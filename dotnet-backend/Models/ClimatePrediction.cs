namespace predictive_climate_control.Models
{
    public class ClimatePrediction
    {
        public float PredictedTemperature { get; set; }
        public float ComfortScore { get; set; }
    }

    public class HvacCommand
    {
        public float HvacSetting { get; set; }
    }
}
