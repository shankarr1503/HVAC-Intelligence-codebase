using Microsoft.AspNetCore.Mvc;
using predictive_climate_control.Models;
using predictive_climate_control.Services;

namespace predictive_climate_control.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ClimateController : ControllerBase
    {
        private readonly ClimateOptimizationService _optimizationService;

        public ClimateController(ClimateOptimizationService optimizationService)
        {
            _optimizationService = optimizationService;
        }

        [HttpPost("/climate/prediction")]
        public ActionResult<ClimatePrediction> Predict([FromBody] SensorData data)
        {
            // call Python AI service via REST/gRPC
            // stubbed response
            return new ClimatePrediction { PredictedTemperature = 22.5 };
        }

        [HttpPost("/hvac/control")]
        public IActionResult Control([FromBody] SensorData data)
        {
            // send HVAC command
            return Ok();
        }
    }
}
