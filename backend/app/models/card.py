from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from ..database import Base

class CardType(enum.Enum):
    DEBIT = "debit"
    CREDIT = "credit"

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, index=True)
    account_id =  Column(Integer, ForeignKey("accounts.id"), nullable=False)
    card_number = Column(String, nullable=False)
    cardholder_name = Column(String, nullable=False, index=True)
    expiry_date = Column(Date, nullable=False, index=True)
    cvv_hash = Column(String, nullable=False)
    card_type = Column(Enum(CardType), nullable=False, index=True)
    is_active = Column(Boolean, nullable=False, default=True)
    is_blocked = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now)

    account = relationship("Account", back_populates="cards")

    def __str__(self):
        return f"Card<id={self.id}, account={self.account_id}, created={self.created_at}, expiry={self.expiry_date}>"
