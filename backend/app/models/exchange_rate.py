from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from ..database import Base

class ExchangeRate(Base):
    __tablename__ = 'exchangerates'

    id = Column(Integer, primary_key=True, index=True)
    from_currency = Column(String, nullable=False)
    to_currency = Column(String, nullable=False)
    rate = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<ExchangeRate(id={self.id}, from={self.from_currency}, to={self.to_currency}, rate={self.rate})>"