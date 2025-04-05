import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { getApiUrl } from '../services/config';

function SetList() {
  const [sets, setSets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSets = async () => {
      try {
        const apiUrl = await getApiUrl();
        const response = await axios.get(`${apiUrl}/sets/`);
        setSets(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch card sets');
        setLoading(false);
      }
    };

    fetchSets();
  }, []);

  if (loading) return <div className="text-center">Loading...</div>;
  if (error) return <div className="text-center text-red-500">{error}</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Pokémon Card Sets</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {sets.map((set) => (
          <Link
            key={set.id}
            to={`/sets/${set.code}`}
            className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow"
          >
            <h2 className="text-xl font-semibold mb-2">{set.name}</h2>
            <p className="text-gray-600">Code: {set.code}</p>
            {set.release_date && (
              <p className="text-gray-600">
                Released: {new Date(set.release_date).toLocaleDateString()}
              </p>
            )}
            {set.total_cards && (
              <p className="text-gray-600">Total Cards: {set.total_cards}</p>
            )}
          </Link>
        ))}
      </div>
    </div>
  );
}

export default SetList; 