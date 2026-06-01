from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Text, Index
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from ..database import Base

class NotificationType(enum.Enum):
    EMAIL = "email"     # Email уведомление
    SMS = "sms"         # SMS сообщение
    PUSH = "push"       # Push-уведомление в приложении

class NotificationPriority(enum.Enum):
    LOW = "low"             # Низкий (можно отложить)
    NORMAL = "normal"       # Обычный
    HIGH = "high"           # Высокий
    CRITICAL = "critical"   # Критический (отправлять мгновенно)


class Notification(Base):
    __tablename__ = 'notifications'
    __table_args__ = (
        Index('ix_notifications_unsent', 'is_sent', 'created_at'),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)               # Получатель уведомления
    type = Column(Enum(NotificationType), nullable=False, default=NotificationType.EMAIL)       # Способ доставки
    priority = Column(Enum(NotificationPriority), default=NotificationPriority.NORMAL)          # Приоритет отправки
    subject = Column(String(200), nullable=True)                                                # Тема (для email) - SMS/PUSH могут без темы
    message = Column(Text, nullable=False)                                                      # Текст сообщения
    delivery_attempts = Column(Integer, default=0)                                              # Количество попыток
    next_retry_at = Column(DateTime, nullable=True)                                             # Когда повторить
    last_error = Column(Text, nullable=True)                                                    # Последняя ошибка
    is_sent = Column(Boolean, default=False)                                                    # Отправлено успешно или нет
    sent_at = Column(DateTime, nullable=True)                                                   # Время успешной отправки
    read_at = Column(DateTime, nullable=True)                                                   # Когда пользователь прочитал
    created_at = Column(DateTime, default=datetime.now)                                         # Время создания уведомления

    user = relationship("User", back_populates='notifications')

    def __repr__(self):
        return f"Notification<id={self.id}, user={self.user_id}, type={self.type}, subject={self.subject}>"