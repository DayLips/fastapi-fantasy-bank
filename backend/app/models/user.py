from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Index
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from ..database import Base

class UserRole(enum.Enum):
    CLIENT = "client"           # Обычный клиент банка
    ADMIN = "admin"             # Администратор (полный доступ)
    OPERATOR = "operator"       # Оператор колл-центра (ограниченный доступ)

class User(Base):
    __tablename__ = 'users'

    __table_args__ = (
        Index('ix_users_full_name', 'last_name', 'first_name', 'second_name'),
    )

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)                    # Email (логин)
    hashed_password = Column(String, nullable=False)                                        # Хеш пароля
    first_name = Column(String(20), nullable=False)                                         # Имя
    second_name = Column(String(20), nullable=False)                                        # Фамилия
    last_name = Column(String(20), nullable=True)                                           # Отчество
    phone = Column(String(20), nullable=False, unique=True)                                 # Телефон
    role = Column(Enum(UserRole), nullable=False, index=True, default=UserRole.CLIENT)      # Роль
    is_active = Column(Boolean, nullable=False, default=True)                               # Активен/заблокирован
    is_verified = Column(Boolean, nullable=False, default=False)                            # Прошел верификацию (email/телефон)
    created_at = Column(DateTime, default=datetime.now)                                     # Дата регистрации
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)              # Дата последнего обновления

    accounts = relationship('Account', back_populates='user')
    payments = relationship('Payment', back_populates='user')
    notifications = relationship('Notification', back_populates='user')
    login_histories = relationship('LoginHistory', back_populates='user')
    audit_logs = relationship('AuditLog', back_populates='user')

    def __repr__(self):
        return f"User<id={self.id}, first_name={self.first_name}, second_name={self.second_name}, last_name={self.last_name}>"
