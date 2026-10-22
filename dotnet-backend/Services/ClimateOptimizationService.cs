using System.Net.Http.Json;
using System.Text.Json.Serialization;
using predictive_climate_control.Models;

namespace predictive_climate_control.Services
{
    /// <summary>Client for the Python AI service (python-ai/services/ai_service_api.py).</summary>
    public class ClimateOptimizationService
    {
        private readonly HttpClient _client;
        private readonly ILogger<ClimateOptimizationService> _logger;

        public ClimateOptimizationService(HttpClient client, ILogger<ClimateOptimizationService> logger)
        {
            _client = client;
            _logger = logger;
        }

        public async Task<ClimatePrediction> PredictAsync(SensorData data, CancellationToken ct = default)
        {
            var prediction = new ClimatePrediction { PredictedTemperature = data.CabinTemp };
            try
            {
                var temp = await PostAsync<TemperatureResponse>("/predict-temperature", ToSensorPayload(data), ct);
                if (temp != null) prediction.PredictedTemperature = temp.PredictedTemp;
                prediction.ComfortScore = await GetComfortScoreAsync(data, ct);
            }
            catch (HttpRequestException ex)
            {
                _logger.LogWarning(ex, "AI service prediction failed; falling back to current cabin temperature");
            }
            return prediction;
        }

        public async Task<float> GetComfortScoreAsync(SensorData data, CancellationToken ct = default)
        {
            var payload = new
            {
                temp = data.CabinTemp,
                humidity = data.Humidity,
                heart_rate = data.HeartRate,
                skin_temp = data.SkinTemperature,
                seat_temp = data.SeatTemperature,
            };
            var result = await PostAsync<ComfortResponse>("/comfort-score", payload, ct);
            return result?.ComfortScore ?? 0f;
        }

        public async Task<HvacCommand> OptimizeAsync(SensorData data, float targetTemp, CancellationToken ct = default)
        {
            var payload = new
            {
                current_temp = data.CabinTemp,
                target_temp = targetTemp,
                outside_temp = data.OutsideTemp,
            };
            var result = await PostAsync<OptimizationResponse>("/optimize-hvac", payload, ct);
            return new HvacCommand { HvacSetting = result?.HvacSetting ?? 0f };
        }

        private async Task<T?> PostAsync<T>(string path, object payload, CancellationToken ct) where T : class
        {
            using var resp = await _client.PostAsJsonAsync(path, payload, ct);
            resp.EnsureSuccessStatusCode();
            return await resp.Content.ReadFromJsonAsync<T>(cancellationToken: ct);
        }

        private static object ToSensorPayload(SensorData data) => new
        {
            cabin_temp = data.CabinTemp,
            outside_temp = data.OutsideTemp,
            humidity = data.Humidity,
            solar_radiation = data.SolarRadiation,
            vehicle_speed = data.VehicleSpeed,
            passenger_count = data.PassengerCount,
            battery_level = data.BatteryLevel,
            hvac_power = data.HvacPower,
            skin_temperature = data.SkinTemperature,
            heart_rate = data.HeartRate,
            seat_temperature = data.SeatTemperature,
            air_quality = data.AirQuality,
        };

        // response shapes of the Python service, which uses snake_case keys
        private sealed class TemperatureResponse
        {
            [JsonPropertyName("predicted_temp")] public float PredictedTemp { get; set; }
        }

        private sealed class ComfortResponse
        {
            [JsonPropertyName("comfort_score")] public float ComfortScore { get; set; }
        }

        private sealed class OptimizationResponse
        {
            [JsonPropertyName("hvac_setting")] public float HvacSetting { get; set; }
        }
    }
}
