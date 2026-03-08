using predictive_climate_control.Models;

namespace predictive_climate_control.Services
{
    public class ClimateOptimizationService
    {
        public ClimatePrediction Optimize(SensorData data)
        {
            // call Python AI service for prediction (REST)
            // this is a synchronous placeholder; in production use IHttpClientFactory
            using var client = new System.Net.Http.HttpClient();
            client.BaseAddress = new System.Uri("http://localhost:8000");
            var postData = new
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
            var resp = client.PostAsJsonAsync("/predict-temperature", postData).Result;
            if (resp.IsSuccessStatusCode)
            {
                var result = resp.Content.ReadFromJsonAsync<ClimatePrediction>().Result;
                return result;
            }
            return new ClimatePrediction { PredictedTemperature = data.CabinTemp };
        }
    }
}
