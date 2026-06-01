from sqlalchemy import Column, Integer, String, DateTime, Numeric, UniqueConstraint, Index
from datetime import datetime

from ..database import Base

class ExchangeRate(Base):
    __tablename__ = 'exchange_rates'
    __table_args__ = (
        UniqueConstraint('from_currency', 'to_currency', name='unique_currency_pair'),
        Index('ix_exchange_rates_updated', 'updated_at'),
    )

    id = Column(Integer, primary_key=True, index=True)
    from_currency = Column(String(3), nullable=False, index=True)                               # Исходная валюта (ISO 4217: USD, EUR, RUB)
    to_currency = Column(String(3), nullable=False, index=True)                                 # Целевая валюта (ISO 4217)
    rate = Column(Numeric(18, 10), nullable=False)                                              # Курс обмена (18 цифр всего, 10 после запятой для криптовалют)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, index=True)      # Время последнего обновления курса

    def __repr__(self):
        return f"<ExchangeRate(id={self.id}, from={self.from_currency}, to={self.to_currency}, rate={self.rate})>"