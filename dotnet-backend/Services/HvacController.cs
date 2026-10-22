using predictive_climate_control.Communication;

namespace predictive_climate_control.Services
{
    public class HvacController
    {
        private readonly CanBusInterface _canBus;

        public HvacController(CanBusInterface canBus)
        {
            _canBus = canBus;
        }

        /// <summary>Send an HVAC power setting (negative cools, positive heats) over the CAN bus.</summary>
        public void SendCommand(float setting)
        {
            _canBus.SendMessage("hvac", BitConverter.GetBytes(setting));
        }
    }
}
