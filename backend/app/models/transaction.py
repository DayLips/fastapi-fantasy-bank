from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, Numeric, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from decimal import Decimal
import enum

from ..database import Base

class TransactionType(enum.Enum):
    TRANSFER = "transfer"           # Перевод между счетами
    DEPOSIT = "deposit"             # Пополнение счета
    WITHDRAWAL = "withdrawal"       # Снятие наличных
    PAYMENT = "payment"             # Оплата услуг/товаров

class TransactionStatus(enum.Enum):
    PENDING = "pending"             # В обработке
    COMPLETED = "completed"         # Выполнена
    FAILED = "failed"               # Ошибка
    CANCELLED = "cancelled"         # Отменена пользователем

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String(36), unique=True, nullable=False, index=True)                                # UUID для идемпотентности
    from_account_id = Column(Integer, ForeignKey("accounts.id"))                                                # Счет отправителя (NULL для пополнений)
    to_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)                                  # Счет получателя (обязательный)
    amount = Column(Numeric(10, 2), nullable=False)                                                             # Сумма транзакции
    currency = Column(String(3), nullable=False, default='RUB')                                                 # Валюта (ISO 4217: RUB, USD, EUR)
    type = Column(Enum(TransactionType), nullable=False, index=True, default=TransactionType.TRANSFER)          # Тип операции
    status = Column(Enum(TransactionStatus), nullable=False, default=TransactionStatus.PENDING, index=True)     # Статус выполнения
    fee = Column(Numeric(10, 2), default=Decimal('0.00'), nullable=False)                                       # Комиссия банка
    description = Column(Text, nullable=True)                                                                   # Назначение платежа (комментарий)  
    created_at = Column(DateTime, default=datetime.now)                                                         # Время создания транзакции
    completed_at = Column(DateTime, nullable=True)                                                              # Время выполнения (заполняется при статусе COMPLETED)

    from_account = relationship("Account", back_populates="outgoing_transactions")
    to_account = relationship("Account", back_populates="incoming_transactions")

    def __repr__(self):
        return f"Transaction<id={self.id}, from={self.from_account_id}, to={self.to_account_id}, amount={self.amount}>"
