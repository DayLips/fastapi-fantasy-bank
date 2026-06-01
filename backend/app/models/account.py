from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from decimal import Decimal
import enum

from ..database import Base

class AccountType(enum.Enum):
    CHECKING = "checking"           # Расчетный счет (для повседневных операций)
    SAVINGS = "savings"             # Накопительный счет (проценты на остаток)
    FOREIGN = "foreign"             # Валютный счет (USD, EUR и т.д.)
    CORPORATE = "corporate"         # Корпоративный счет (для юр. лиц)

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)  
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)                       # Владелец счета
    account_type = Column(Enum(AccountType), default=AccountType.CHECKING, nullable=False)              # Тип счета
    account_number = Column(String(34), nullable=False, unique=True, index=True)                        # Номер счета (IBAN, до 34 символов)
    balance = Column(Numeric(10, 2), default=Decimal('0.00'), nullable=False)                           # Текущий баланс (деньги, 2 знака)
    daily_limit = Column(Numeric(10, 2), default=Decimal('100000.00'), nullable=False)                  # Лимит операций в день
    monthly_limit = Column(Numeric(10, 2), default=Decimal('1000000.00'), nullable=False)               # Лимит операций в месяц
    single_transaction_limit = Column(Numeric(10, 2), default=Decimal('50000.00'), nullable=False)      # Лимит одной транзакции
    currency = Column(String(3), nullable=False, default='RUB')                                         # Валюта счета (ISO 4217)
    is_active = Column(Boolean, nullable=False, default=True)                                           # Активен ли счет (не закрыт)
    created_at = Column(DateTime, default=datetime.now)                                                 # Дата открытия счета
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)                          # Дата последней операции

    user = relationship("User", back_populates='accounts')
    outgoing_transactions = relationship("Transaction", foreign_keys="Transaction.from_account_id", back_populates="from_account")
    incoming_transactions = relationship("Transaction", foreign_keys="Transaction.to_account_id", back_populates="to_account")
    cards = relationship("Card", foreign_keys="Card.account_id", back_populates="account")
    payments = relationship("Payment", foreign_keys="Payment.account_id", back_populates="account")

    def __repr__(self):
        return f"Account<id={self.id}, account_number={self.account_number}, balance={self.balance}, currency={self.currency}>"