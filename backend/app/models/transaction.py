from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String(36), unique=True, nullable=False, index=True)
    from_account_id = Column(Integer, ForeignKey("accounts.id"))
    to_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String, nullable=False)
    type = Column(String(15), nullable=False, index=True, default='transfer')
    status = Column(String(15), nullable=False, default="pending")
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    completed_at = Column(DateTime)

    from_account = relationship("Account", back_populates="outgoing_transactions")
    to_account = relationship("Account", back_populates="incoming_transactions")

    def __repr__(self):
        return f"Transaction<id={self.id}, from={self.from_account_id}, to={self.to_account_id}, amount={self.amount}>"
