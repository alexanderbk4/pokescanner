-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS pokemon_cards;
USE pokemon_cards;

-- Cards table
CREATE TABLE IF NOT EXISTS cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    set_name VARCHAR(255) NOT NULL,
    set_code VARCHAR(50) NOT NULL,
    card_number VARCHAR(50) NOT NULL,
    rarity VARCHAR(50) NOT NULL,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_card (set_code, card_number)
);

-- Card sets table
CREATE TABLE IF NOT EXISTS card_sets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(50) NOT NULL,
    release_date DATE,
    total_cards INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_set_code (code)
);

-- Create indexes for better query performance
CREATE INDEX idx_card_name ON cards(name);
CREATE INDEX idx_set_code ON cards(set_code); 