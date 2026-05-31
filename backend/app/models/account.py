from sqlalchemy import Column, Integer, String, Boolean, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from decimal import Decimal

from ..database import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_number = Column(String, nullable=False)
    balance = Column(DECIMAL(scale=2), default=Decimal('0.0'), nullable=False)
    currency = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    uploated_at = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates='accounts')

    def __repr__(self):
        return f"Account<id={self.id}, account_number={self.account_number}, balance={self.balance}, currency={self.currency}>"