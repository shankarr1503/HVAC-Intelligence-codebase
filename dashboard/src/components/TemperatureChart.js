import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Legend,
  Tooltip,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

// Chart.js v3 is tree-shakeable: scales and elements must be registered
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Legend, Tooltip);

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
