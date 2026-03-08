import React from 'react';
import { Line } from 'react-chartjs-2';

const TemperatureChart = ({ data }) => {
  const chartData = {
    labels: data.map((_, i) => i),
    datasets: [{
      label: 'Cabin Temp',
      data,
      borderColor: 'rgba(75,192,192,1)',
    }]
  };
  return <Line data={chartData} />;
};

export default TemperatureChart;
