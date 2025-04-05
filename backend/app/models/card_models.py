from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.database import Base

class Rarity(enum.Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    RARE_HOLO = "Rare Holo"

class CardSet(Base):
    """Model for Pokemon card sets."""
    __tablename__ = "card_sets"

    id = Column(Integer, primary_key=True)
    set_id = Column(String(50), unique=True, nullable=False)  # e.g., 'base1'
    name = Column(String(100), nullable=False)  # e.g., 'Base'
    series = Column(String(100))  # e.g., 'Base'
    printed_total = Column(Integer)  # Total cards in set
    total = Column(Integer)  # Total cards in set including variants
    release_date = Column(DateTime)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    cards = relationship("Card", back_populates="card_set")

class Card(Base):
    """Model for individual Pokemon cards."""
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    card_id = Column(String(50), unique=True, nullable=False)  # TCG API ID
    name = Column(String(100), nullable=False)
    number = Column(String(20), nullable=False)  # Card number in set
    rarity = Column(String(50))  # Using String instead of Enum for flexibility
    image_url = Column(String(500))  # High-res image
    image_small_url = Column(String(500))  # Small image
    
    # Card details
    supertype = Column(String(50))  # Pokemon, Trainer, Energy
    subtypes = Column(JSON)  # List of subtypes
    types = Column(JSON)  # Pokemon types (Fire, Water, etc.)
    hp = Column(Integer)  # HP for Pokemon cards
    rules = Column(JSON)  # Card rules text
    
    # Set relationship
    set_id = Column(Integer, ForeignKey('card_sets.id'), nullable=False)
    card_set = relationship("CardSet", back_populates="cards")
    
    # Price history
    prices = relationship("CardPrice", back_populates="card")
    
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class CardPrice(Base):
    """Model for tracking card price history."""
    __tablename__ = "card_prices"

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey('cards.id'), nullable=False)
    
    # Different price points
    normal_low = Column(Float)
    normal_mid = Column(Float)
    normal_high = Column(Float)
    normal_market = Column(Float)
    
    holofoil_low = Column(Float)
    holofoil_mid = Column(Float)
    holofoil_high = Column(Float)
    holofoil_market = Column(Float)
    
    # When these prices were recorded
    recorded_at = Column(DateTime, server_default=func.now(), nullable=False)
    
    # Relationship
    card = relationship("Card", back_populates="prices") 