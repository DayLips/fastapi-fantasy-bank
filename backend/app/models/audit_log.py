from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from ..database import Base

class AuditLogAction(enum.Enum):
    LOGIN = 'login'                     # Вход в систему
    TRANSFER = 'transfer'               # Перевод денег
    UPDATE_PROFILE = 'update_profile'   # Обновление профиля
    ETC = 'etc'                         # Другие действия (расширяемый список)


class AuditLog(Base):
    __tablename__ = 'audit_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)        # Кто выполнил действие (NULL - система)
    action = Column(Enum(AuditLogAction), nullable=False, index=True)                   # Тип действия
    entity_type = Column(String(50), nullable=False, index=True)                        # Тип сущности (user/account/transaction)
    entity_id = Column(Integer, nullable=True)                                          # ID сущности, над которой действие
    old_value = Column(JSON)                                                            # Старое значение (JSON: {"balance": 1000})
    new_value = Column(JSON)                                                            # Новое значение (JSON: {"balance": 950})
    ip_address = Column(String(45), nullable=True)                                      # IP-адрес, с которого выполнено действие
    created_at = Column(DateTime, default=datetime.now)                                 # Время выполнения действия

    user = relationship('User', back_populates='audit_logs')

    def __repr__(self):
        return f"AuditLog<id={self.id}, user_id={self.user_id}, ip_address={self.ip_address}, action={self.action}>"
