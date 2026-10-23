import React, { useEffect, useState } from 'react';
import TemperatureChart from './components/TemperatureChart';
import ComfortScore from './components/ComfortScore';

const TELEMETRY_URL = process.env.REACT_APP_TELEMETRY_URL || 'ws://localhost:5000/ws/telemetry';
// keep only the most recent samples so the page doesn't grow without bound
const MAX_POINTS = 100;
const RECONNECT_MS = 3000;

const append = (list, value) => [...list, value].slice(-MAX_POINTS);

function App() {
  const [data, setData] = useState({temp: [], comfort: []});

  useEffect(() => {
    let socket;
    let reconnectTimer;
    let closed = false;

    const connect = () => {
      socket = new WebSocket(TELEMETRY_URL);
      socket.onmessage = (event) => {
        const msg = JSON.parse(event.data);
        setData(prev => ({
          temp: append(prev.temp, msg.cabin_temp),
          comfort: append(prev.comfort, msg.comfort_score)
        }));
      };
      socket.onclose = () => {
        if (!closed) reconnectTimer = setTimeout(connect, RECONNECT_MS);
      };
    };
    connect();

    return () => {
      closed = true;
      clearTimeout(reconnectTimer);
      socket.close();
    };
  }, []);

  return (
    <div>
      <h1>Climate Dashboard</h1>
      <TemperatureChart data={data.temp} />
      <ComfortScore data={data.comfort} />
    </div>
  );
}

export default App;
