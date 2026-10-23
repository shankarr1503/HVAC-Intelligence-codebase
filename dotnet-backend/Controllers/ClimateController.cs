using Microsoft.AspNetCore.Mvc;
using predictive_climate_control.Models;
using predictive_climate_control.Services;

namespace predictive_climate_control.Controllers
{
    [ApiController]
    public class ClimateController : ControllerBase
    {
        private const float DefaultTargetTemp = 22f;

        private readonly ClimateOptimizationService _optimizationService;
        private readonly HvacController _hvac;

        public ClimateController(ClimateOptimizationService optimizationService, HvacController hvac)
        {
            _optimizationService = optimizationService;
            _hvac = hvac;
        }

        [HttpPost("/climate/prediction")]
        public async Task<ActionResult<ClimatePrediction>> Predict([FromBody] SensorData data, CancellationToken ct)
        {
            return await _optimizationService.PredictAsync(data, ct);
        }

        [HttpPost("/hvac/control")]
        public async Task<ActionResult<HvacCommand>> Control([FromBody] SensorData data,
            [FromQuery] float targetTemp = DefaultTargetTemp, CancellationToken ct = default)
        {
            try
            {
                var command = await _optimizationService.OptimizeAsync(data, targetTemp, ct);
                _hvac.SendCommand(command.HvacSetting);
                return command;
            }
            catch (HttpRequestException)
            {
                return StatusCode(StatusCodes.Status502BadGateway, "AI service unavailable");
            }
        }
    }
}
