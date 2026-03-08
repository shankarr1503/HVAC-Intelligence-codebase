using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace predictive_climate_control.Communication
{
    public class CanBusInterface
    {
        private readonly Queue<Tuple<string, byte[]>> _inbox = new();

        // event raised when a message is received
        public event Action<string, byte[]> OnMessageReceived;

        public void SendMessage(string id, byte[] payload)
        {
            // in simulation just enqueue and fire event asynchronously
            Task.Run(() =>
            {
                _inbox.Enqueue(Tuple.Create(id, payload));
                OnMessageReceived?.Invoke(id, payload);
            });
        }

        public byte[] ReceiveMessage()
        {
            if (_inbox.Count > 0)
            {
                var msg = _inbox.Dequeue();
                return msg.Item2;
            }
            return Array.Empty<byte>();
        }

        // helper to simulate periodic telemetry
        public void SimulateTelemetry(float cabinTemp, float hvacPower)
        {
            var payload = BitConverter.GetBytes(cabinTemp);
            SendMessage("temp", payload);
        }
    }
}
