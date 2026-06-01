from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, Enum, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from decimal import Decimal
import enum

from ..database import Base

class CardType(enum.Enum):
    DEBIT = "debit"     # Дебетовая карта (свои деньги)
    CREDIT = "credit"   # Кредитная карта (деньги банка)

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, index=True)
    account_id =  Column(Integer, ForeignKey("accounts.id"), nullable=False)        # К какому счету привязана карта
    card_number_hash  = Column(String(64), nullable=False, unique=True)             # Хеш полного номера карты
    card_number_masked = Column(String(19), nullable=False)                         # Маскированный номер для отображения (**** **** **** 1234)
    cardholder_name = Column(String, nullable=False, index=True)                    # Имя держателя карты (латиницей)
    expiry_date = Column(Date, nullable=False)                                      # Срок действия (MM/YY)
    cvv_hash = Column(String, nullable=False)                                       # Хеш CVV-кода
    card_type = Column(Enum(CardType), nullable=False, index=True)                  # Тип карты
    pin_hash = Column(String(64), nullable=False)                                   # Хеш PIN-кода
    pin_attempts = Column(Integer, default=0)                                       # Счетчик неверных попыток
    pin_blocked_until = Column(DateTime, nullable=True)                             # Блокировка после 3 попыток
    daily_atm_limit = Column(Numeric(10, 2), default=Decimal('50000.00'))           # Лимит снятия наличных в день
    daily_payment_limit = Column(Numeric(10, 2), default=Decimal('100000.00'))      # Лимит оплаты в день
    contactless_enabled = Column(Boolean, default=True)                             # Включена ли бесконтактная оплата
    issued_at = Column(DateTime, default=datetime.now)                              # Когда выпущена
    activated_at = Column(DateTime, nullable=True)                                  # Когда активирована
    is_active = Column(Boolean, nullable=False, default=True)                       # Активна ли карта
    is_blocked = Column(Boolean, nullable=False, default=False)                     # Заблокирована (потеря/кража)
    created_at = Column(DateTime, default=datetime.now)                             # Время создания записи в БД

    account = relationship("Account", back_populates="cards")

    def __repr__(self):
        return f"Card<id={self.id}, account={self.account_id}, created={self.created_at}, expiry={self.expiry_date}>"
