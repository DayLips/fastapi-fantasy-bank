from sqlalchemy import Column, Integer, String, DateTime, Enum, Numeric
from datetime import datetime
import enum

from ..database import Base

class ATMStatus(enum.Enum):
    ACTIVE = "active"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"

class ATM(Base):
    __tablename__ = 'atms'

    id = Column(Integer, primary_key=True, index=True)
    atm_code = Column(String, nullable=False)
    address = Column(String, nullable=False)
    lattitude = Column(Numeric(10, 2), nullable=False)
    longitude = Column(Numeric(10, 2), nullable=False)
    status = Column(Enum(ATMStatus), nullable=False, index=True, default=ATMStatus.ACTIVE)
    cash_balance = Column(Numeric(10, 2), nullable=False)
    last_maintenance_date = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"ATM<id={self.id}, address={self.address}, cash_balance={self.cash_balance}, status={self.status}>"