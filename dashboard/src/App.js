import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import TemperatureChart from './components/TemperatureChart';
import ComfortScore from './components/ComfortScore';

const socket = io('http://localhost:5000');

function App() {
  const [data, setData] = useState({temp: [], comfort: []});

  useEffect(() => {
    socket.on('telemetry', (msg) => {
      setData(prev => ({
        temp: [...prev.temp, msg.cabin_temp],
        comfort: [...prev.comfort, msg.comfort_score]
      }));
    });
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
