using System.Text.Json;
using predictive_climate_control.Models;
using predictive_climate_control.Streaming;

namespace predictive_climate_control.Services
{
    public class TelemetryService
    {
        private readonly WebSocketService _webSocket;

        public TelemetryService(WebSocketService webSocket)
        {
            _webSocket = webSocket;
        }

        /// <summary>Push a telemetry sample to connected dashboard clients.</summary>
        public Task StreamTelemetryAsync(SensorData data, float comfortScore, CancellationToken ct = default)
        {
            var message = JsonSerializer.Serialize(new
            {
                cabin_temp = data.CabinTemp,
                comfort_score = comfortScore,
            });
            return _webSocket.BroadcastAsync(message, ct);
        }
    }
}
