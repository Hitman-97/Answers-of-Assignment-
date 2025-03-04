import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/data')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
      });
  }, []);

  return (
    <div className="App">
      <h1>AI-Powered Web Crawler Dashboard</h1>
      {data.length > 0 ? (
        data.map((page, index) => (
          <div key={index}>
            <h2>{page.title}</h2>
            <p><strong>Category:</strong> {page.ai_analysis}</p>
            <p><strong>Sentiment:</strong> {page.ai_analysis}</p>
            <p><strong>Summary:</strong> {page.ai_analysis}</p>
            <p><strong>Metadata:</strong> {page.metadata.join(', ')}</p>
          </div>
        ))
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default App;
