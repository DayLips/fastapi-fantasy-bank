from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from ..database import Base

class PaymentStatus(enum.Enum):
    DRAFT = "draft"
    EXECUTED = "executed"
    CANCELLED = "cancelled"

class Payment(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    payee_name = Column(String(20), nullable=False)
    inn = Column(String, nullable=False)
    purpose = Column(String, nullable=False)
    status = Column(Enum(PaymentStatus), nullable=False, index=True, default=PaymentStatus.DRAFT)
    created_at = Column(DateTime, default=datetime.now)
    executed_at = Column(DateTime)

    user = relationship("User", back_populates='payments')
    account = relationship("User", back_populates='payments')

    def __repr__(self):
        return f"Payment<id={self.id}, account={self.account_id}, created={self.created_at}, amount={self.amount}, status={self.status}>"