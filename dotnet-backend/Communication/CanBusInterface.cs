using System;
using System.Collections.Concurrent;
using System.Threading.Tasks;

namespace predictive_climate_control.Communication
{
    public class CanBusInterface
    {
        private readonly ConcurrentQueue<Tuple<string, byte[]>> _inbox = new();

        // event raised when a message is received
        public event Action<string, byte[]>? OnMessageReceived;

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
            return _inbox.TryDequeue(out var msg) ? msg.Item2 : Array.Empty<byte>();
        }

        // helper to simulate periodic telemetry
        public void SimulateTelemetry(float cabinTemp, float hvacPower)
        {
            SendMessage("temp", BitConverter.GetBytes(cabinTemp));
            SendMessage("hvac_power", BitConverter.GetBytes(hvacPower));
        }
    }
}
