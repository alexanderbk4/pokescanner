from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    set_name = Column(String(255), nullable=False)
    set_code = Column(String(50), nullable=False)
    card_number = Column(String(50), nullable=False)
    rarity = Column(String(50), nullable=False)
    pricecharting_id = Column(String(100))
    image_url = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationships
    price_history = relationship("PriceHistory", back_populates="card", cascade="all, delete-orphan")

class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    low_price = Column(Float)
    mid_price = Column(Float)
    high_price = Column(Float)
    recorded_at = Column(TIMESTAMP, server_default=func.now())

    # Relationships
    card = relationship("Card", back_populates="price_history")

class CardSet(Base):
    __tablename__ = "card_sets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    code = Column(String(50), nullable=False, unique=True)
    release_date = Column(Date)
    total_cards = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now()) 