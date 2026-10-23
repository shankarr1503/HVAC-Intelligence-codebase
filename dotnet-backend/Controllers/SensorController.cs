using Microsoft.AspNetCore.Mvc;
using predictive_climate_control.Models;
using predictive_climate_control.Services;

namespace predictive_climate_control.Controllers
{
    [ApiController]
    [Route("sensor-data")]
    public class SensorController : ControllerBase
    {
        private readonly ClimateOptimizationService _optimizationService;
        private readonly TelemetryService _telemetry;
        private readonly ILogger<SensorController> _logger;

        public SensorController(ClimateOptimizationService optimizationService, TelemetryService telemetry,
            ILogger<SensorController> logger)
        {
            _optimizationService = optimizationService;
            _telemetry = telemetry;
            _logger = logger;
        }

        [HttpPost]
        public async Task<IActionResult> PostSensorData([FromBody] SensorData data, CancellationToken ct)
        {
            float comfort = 0f;
            try
            {
                comfort = await _optimizationService.GetComfortScoreAsync(data, ct);
            }
            catch (HttpRequestException ex)
            {
                _logger.LogWarning(ex, "Comfort scoring failed; streaming telemetry without it");
            }
            await _telemetry.StreamTelemetryAsync(data, comfort, ct);
            return Ok();
        }
    }
}
