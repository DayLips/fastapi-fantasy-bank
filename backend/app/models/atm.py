from sqlalchemy import Column, Integer, String, DateTime, Enum, Numeric, Boolean
from decimal import Decimal
import enum

from ..database import Base

class ATMStatus(enum.Enum):
    ACTIVE = "active"               # Работает
    MAINTENANCE = "maintenance"     # На техобслуживании
    OFFLINE = "offline"             # Отключен (нет связи/сломан)

class ATM(Base):
    __tablename__ = 'atms'

    id = Column(Integer, primary_key=True, index=True)
    atm_code = Column(String(20), nullable=False)                                                   # Внутренний код/номер банкомата
    address = Column(String(300), nullable=False)                                                   # Адрес установки
    latitude = Column(Numeric(10, 7), nullable=False)                                               # Широта
    longitude = Column(Numeric(10, 7), nullable=False)                                              # Долгота
    status = Column(Enum(ATMStatus), nullable=False, index=True, default=ATMStatus.ACTIVE)          # Текущий статус
    cash_balance = Column(Numeric(10, 2), nullable=False)                                           # Остаток наличных в банкомате
    last_maintenance_date = Column(DateTime, nullable=True)                                         # Дата последнего техобслуживания
    city = Column(String(100), nullable=True, index=True)                                           # Город для поиска
    currency = Column(String(3), nullable=False, default='RUB')                                     # Валюта банкомата
    max_withdrawal = Column(Numeric(10, 2), default=Decimal('50000.00'))                            # Макс. сумма выдачи
    is_deposit_available = Column(Boolean, default=False)                                           # Есть ли прием наличных
    last_checked_at = Column(DateTime, nullable=True)                                               # Последняя проверка связи

    def __repr__(self):
        return f"ATM<id={self.id}, address={self.address}, cash_balance={self.cash_balance}, status={self.status}>"