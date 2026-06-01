from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, Numeric, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from ..database import Base

class TransactionType(enum.Enum):
    TRANSFER = "transfer"
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    PAYMENT = "payment"

class TransactionStatus(enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String(36), unique=True, nullable=False, index=True)
    from_account_id = Column(Integer, ForeignKey("accounts.id"))
    to_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String, nullable=False)
    type = Column(Enum(TransactionType), nullable=False, index=True, default=TransactionType.TRANSFER)
    status = Column(Enum(TransactionStatus), nullable=False, default=TransactionStatus.PENDING)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    completed_at = Column(DateTime)

    from_account = relationship("Account", back_populates="outgoing_transactions")
    to_account = relationship("Account", back_populates="incoming_transactions")

    def __repr__(self):
        return f"Transaction<id={self.id}, from={self.from_account_id}, to={self.to_account_id}, amount={self.amount}>"
