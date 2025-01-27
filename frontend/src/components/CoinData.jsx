import { useEffect, useState } from 'react';
import './CoinData.css';

function CoinData() {
  const [coinData, setCoinData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchCoinData() {
      try {
        const response = await fetch('http://localhost:5000/api/coin-data');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setCoinData(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    }

    fetchCoinData();
  }, []);

  if (loading) return <div className="loading">Loading coin data...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="coin-data-container">
      <h2>{coinData.name} ({coinData.symbol.toUpperCase()})</h2>
      <div className="data-grid">
        <div className="data-item">
          <span className="label">Price:</span>
          <span className="value">${coinData.price_usd}</span>
        </div>
        <div className="data-item">
          <span className="label">Market Cap:</span>
          <span className="value">${coinData.market_cap_usd.toLocaleString()}</span>
        </div>
        <div className="data-item">
          <span className="label">Volume (24h):</span>
          <span className="value">${coinData.volume_usd.toLocaleString()}</span>
        </div>
      </div>
    </div>
  );
}

export default CoinData;
