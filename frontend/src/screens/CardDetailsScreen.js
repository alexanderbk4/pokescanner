import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Image, ScrollView } from 'react-native';

const CardDetailsScreen = ({ route }) => {
  const [card, setCard] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // TODO: Fetch card details from API
    // This is a placeholder for the actual API call
    const fetchCardDetails = async () => {
      try {
        // Simulated API call
        setTimeout(() => {
          setCard({
            name: 'Charizard',
            set: 'Base Set',
            number: '4/102',
            rarity: 'Rare Holo',
            price: {
              low: 150.00,
              mid: 175.00,
              high: 200.00
            },
            imageUrl: 'https://example.com/charizard.jpg'
          });
          setLoading(false);
        }, 1000);
      } catch (error) {
        console.error('Error fetching card details:', error);
        setLoading(false);
      }
    };

    fetchCardDetails();
  }, []);

  if (loading) {
    return (
      <View style={styles.container}>
        <Text>Loading...</Text>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container}>
      <View style={styles.cardContainer}>
        <Image
          source={{ uri: card.imageUrl }}
          style={styles.cardImage}
          resizeMode="contain"
        />
        <View style={styles.detailsContainer}>
          <Text style={styles.cardName}>{card.name}</Text>
          <Text style={styles.cardSet}>{card.set}</Text>
          <Text style={styles.cardNumber}>#{card.number}</Text>
          <Text style={styles.rarity}>{card.rarity}</Text>
          
          <View style={styles.priceContainer}>
            <Text style={styles.priceTitle}>Current Prices:</Text>
            <View style={styles.priceRow}>
              <Text style={styles.priceLabel}>Low:</Text>
              <Text style={styles.priceValue}>${card.price.low.toFixed(2)}</Text>
            </View>
            <View style={styles.priceRow}>
              <Text style={styles.priceLabel}>Mid:</Text>
              <Text style={styles.priceValue}>${card.price.mid.toFixed(2)}</Text>
            </View>
            <View style={styles.priceRow}>
              <Text style={styles.priceLabel}>High:</Text>
              <Text style={styles.priceValue}>${card.price.high.toFixed(2)}</Text>
            </View>
          </View>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  cardContainer: {
    padding: 20,
    alignItems: 'center',
  },
  cardImage: {
    width: '100%',
    height: 400,
    marginBottom: 20,
  },
  detailsContainer: {
    width: '100%',
    backgroundColor: 'white',
    padding: 20,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  cardName: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  cardSet: {
    fontSize: 18,
    color: '#666',
    marginBottom: 5,
  },
  cardNumber: {
    fontSize: 16,
    color: '#666',
    marginBottom: 5,
  },
  rarity: {
    fontSize: 16,
    color: '#f4511e',
    marginBottom: 20,
  },
  priceContainer: {
    marginTop: 20,
  },
  priceTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  priceRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 5,
  },
  priceLabel: {
    fontSize: 16,
    color: '#666',
  },
  priceValue: {
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default CardDetailsScreen; 