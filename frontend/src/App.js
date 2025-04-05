import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [cards, setCards] = useState([]);
  const [sets, setSets] = useState([]);
  const [selectedSet, setSelectedSet] = useState('base1'); // Default to Base Set
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch sets
    fetch('http://localhost:8003/sets/')
      .then(response => response.json())
      .then(data => {
        setSets(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching sets:', error);
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    // Fetch cards when selectedSet changes
    if (selectedSet) {
      setLoading(true);
      fetch(`http://localhost:8003/cards/?set_name=${selectedSet}`)
        .then(response => response.json())
        .then(data => {
          setCards(data);
          setLoading(false);
        })
        .catch(error => {
          console.error('Error fetching cards:', error);
          setLoading(false);
        });
    }
  }, [selectedSet]);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8 text-gray-800">Pokémon Card Scanner</h1>
        
        {/* Set Selection */}
        <div className="mb-8">
          <label htmlFor="set-select" className="block text-sm font-medium text-gray-700 mb-2">
            Select Set:
          </label>
          <select
            id="set-select"
            value={selectedSet}
            onChange={(e) => setSelectedSet(e.target.value)}
            className="block w-full max-w-md rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          >
            {sets.map(set => (
              <option key={set.id} value={set.code}>
                {set.name}
              </option>
            ))}
          </select>
        </div>

        {/* Loading State */}
        {loading && (
          <div className="text-center">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-4 border-gray-300 border-t-indigo-600"></div>
            <p className="mt-2 text-gray-600">Loading cards...</p>
          </div>
        )}

        {/* Cards Grid */}
        {!loading && (
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
            {cards.map(card => (
              <div key={card.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                <div className="aspect-w-1 aspect-h-1">
                  {card.image_url ? (
                    <img
                      src={card.image_url}
                      alt={card.name}
                      className="object-cover w-full h-full"
                      onError={(e) => {
                        e.target.src = 'https://via.placeholder.com/245x342?text=No+Image';
                      }}
                    />
                  ) : (
                    <div className="w-full h-full bg-gray-200 flex items-center justify-center">
                      <span className="text-gray-500">No Image</span>
                    </div>
                  )}
                </div>
                <div className="p-4">
                  <h3 className="text-lg font-semibold text-gray-800 mb-1">{card.name}</h3>
                  <p className="text-sm text-gray-600 mb-1">#{card.card_number}</p>
                  <p className="text-sm text-gray-600">Rarity: {card.rarity}</p>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* No Cards Message */}
        {!loading && cards.length === 0 && (
          <div className="text-center text-gray-600">
            <p>No cards found for this set.</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App; 