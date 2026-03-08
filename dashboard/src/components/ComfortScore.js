import React from 'react';

const ComfortScore = ({ data }) => (
  <div>
    <h2>Comfort Score</h2>
    <ul>
      {data.map((score, idx) => <li key={idx}>{score.toFixed(2)}</li>)}
    </ul>
  </div>
);

export default ComfortScore;
