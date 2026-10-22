using System.Collections.Concurrent;
using System.Net.WebSockets;
using System.Text;

namespace predictive_climate_control.Streaming
{
    public class WebSocketService
    {
        private readonly ConcurrentDictionary<Guid, WebSocket> _clients = new();
        // a WebSocket allows only one outstanding send, so broadcasts are serialized
        private readonly SemaphoreSlim _sendLock = new(1, 1);

        /// <summary>Keep a client registered until it disconnects.</summary>
        public async Task HandleClientAsync(WebSocket socket, CancellationToken ct)
        {
            var id = Guid.NewGuid();
            _clients[id] = socket;
            var buffer = new byte[1024];
            try
            {
                while (socket.State == WebSocketState.Open && !ct.IsCancellationRequested)
                {
                    var result = await socket.ReceiveAsync(new ArraySegment<byte>(buffer), ct);
                    if (result.MessageType == WebSocketMessageType.Close)
                    {
                        await socket.CloseAsync(WebSocketCloseStatus.NormalClosure, null, CancellationToken.None);
                    }
                }
            }
            catch (OperationCanceledException) { }
            catch (WebSocketException) { }
            finally
            {
                _clients.TryRemove(id, out _);
            }
        }

        public async Task BroadcastAsync(string message, CancellationToken ct = default)
        {
            var bytes = new ArraySegment<byte>(Encoding.UTF8.GetBytes(message));
            await _sendLock.WaitAsync(ct);
            try
            {
                foreach (var (id, socket) in _clients)
                {
                    if (socket.State != WebSocketState.Open)
                    {
                        _clients.TryRemove(id, out _);
                        continue;
                    }
                    try
                    {
                        await socket.SendAsync(bytes, WebSocketMessageType.Text, true, ct);
                    }
                    catch (WebSocketException)
                    {
                        _clients.TryRemove(id, out _);
                    }
                }
            }
            finally
            {
                _sendLock.Release();
            }
        }
    }
}
