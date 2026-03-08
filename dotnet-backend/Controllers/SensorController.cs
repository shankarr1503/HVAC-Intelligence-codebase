using Microsoft.AspNetCore.Mvc;
using predictive_climate_control.Models;

namespace predictive_climate_control.Controllers
{
    [ApiController]
    [Route("sensor-data")]
    public class SensorController : ControllerBase
    {
        [HttpPost]
        public IActionResult PostSensorData([FromBody] SensorData data)
        {
            // ingest and forward to AI service
            return Ok();
        }
    }
}
