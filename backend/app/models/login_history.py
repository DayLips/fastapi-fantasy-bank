from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database import Base

class LoginHistory(Base):
    __tablename__ = 'login_histories'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)        # ID пользователя (NULL - несуществующий email)
    session_id = Column(String(36), unique=True, nullable=True, index=True)             # UUID сессии для отслеживания активности
    ip_address = Column(String(45), nullable=False)                                     # IP-адрес (IPv4 - 15, IPv6 - до 45 символов)
    user_agent = Column(Text, nullable=True)                                            # Информация о браузере/устройстве
    login_time = Column(DateTime, default=datetime.now, nullable=False, index=True)     # Время попытки входа
    logout_time = Column(DateTime, nullable=True)                                       # Время выхода (для расчета длительности сессии)
    success = Column(Boolean, default=False, index=True)                                # Успешный вход или нет

    user = relationship("User", back_populates='login_histories')

    def __repr__(self):
        return f"LoginHistory<id={self.id}, user_id={self.user_id}, ip_address={self.ip_address}>"

