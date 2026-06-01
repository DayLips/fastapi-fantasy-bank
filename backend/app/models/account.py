from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from decimal import Decimal

from ..database import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_number = Column(String, nullable=False, unique=True)
    balance = Column(Numeric(10, 2), default=Decimal('0.00'), nullable=False)
    currency = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates='accounts')
    outgoing_transactions = relationship("Transaction", foreign_keys="Transaction.from_account_id", back_populates="from_account")
    incoming_transactions = relationship("Transaction", foreign_keys="Transaction.to_account_id", back_populates="to_account")
    cards = relationship("Card", foreign_keys="Card.account_id", back_populates="account")
    payments = relationship("Payment", foreign_keys="Payment.account_id", back_populates="payment")

    def __repr__(self):
        return f"Account<id={self.id}, account_number={self.account_number}, balance={self.balance}, currency={self.currency}>"