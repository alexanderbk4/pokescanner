import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { getApiUrl } from '../services/config';

function CardList() {
  const { setCode } = useParams();
  const [cards, setCards] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCards = async () => {
      try {
        const apiUrl = await getApiUrl();
        const response = await axios.get(`${apiUrl}/cards/set/${setCode}`);
        setCards(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch cards');
        setLoading(false);
      }
    };

    fetchCards();
  }, [setCode]);

  if (loading) return <div className="text-center">Loading...</div>;
  if (error) return <div className="text-center text-red-500">{error}</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Cards in Set</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {cards.map((card) => (
          <div
            key={card.id}
            className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow"
          >
            <h2 className="text-xl font-semibold mb-2">{card.name}</h2>
            <p className="text-gray-600">Card Number: {card.card_number}</p>
            <p className="text-gray-600">Rarity: {card.rarity}</p>
            {card.image_url && (
              <div className="mt-4">
                <img
                  src={card.image_url}
                  alt={card.name}
                  className="w-full h-auto rounded"
                />
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default CardList; 