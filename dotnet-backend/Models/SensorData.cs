namespace predictive_climate_control.Models
{
    public class SensorData
    {
        public float CabinTemp { get; set; }
        public float OutsideTemp { get; set; }
        public float Humidity { get; set; }
        public float SolarRadiation { get; set; }
        public float VehicleSpeed { get; set; }
        public int PassengerCount { get; set; }
        public float BatteryLevel { get; set; }
        public float HvacPower { get; set; }
        public float SkinTemperature { get; set; }
        public float HeartRate { get; set; }
        public float SeatTemperature { get; set; }
        public float AirQuality { get; set; }
    }
}
