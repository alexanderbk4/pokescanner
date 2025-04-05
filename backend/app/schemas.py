from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date

class CardBase(BaseModel):
    name: str
    set_name: str
    set_code: str
    card_number: str
    rarity: str
    image_url: Optional[str] = None

class CardCreate(CardBase):
    pass

class Card(CardBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CardSetBase(BaseModel):
    name: str
    code: str
    release_date: Optional[date] = None
    total_cards: Optional[int] = None

class CardSetCreate(CardSetBase):
    pass

class CardSet(CardSetBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CardSetWithCards(CardSet):
    cards: List[Card] = [] 