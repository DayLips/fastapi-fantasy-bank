from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from ..database import Base

class UserRole(enum.Enum):
    CLIENT = "client"
    ADMIN = "admin"
    OPERATOR = "operator"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String(20), nullable=False, index=True)
    second_name = Column(String(20), nullable=False, index=True)
    last_name = Column(String(20), nullable=False, index=True)
    phone = Column(String(20), nullable=False)
    role = Column(Enum(UserRole), nullable=False, index=True, default=UserRole.CLIENT)
    is_active = Column(Boolean, nullable=False, default=True)
    is_verified = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    accounts = relationship('Account', foreign_keys="Account.user_id", back_populates='user')
    payments = relationship('Payment', foreign_keys='Payment.user_id', back_populates='payment')
    notifications = relationship('Notification', foreign_keys="Notification.user_id", back_populates='notification')

    def __repr__(self):
        return f"User<id={self.id}, first_name={self.first_name}, second_name={self.second_name}, last_name={self.last_name}>"
