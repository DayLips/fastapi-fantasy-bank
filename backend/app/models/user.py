from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String(20), nullable=False, index=True)
    second_name = Column(String(20), nullable=False, index=True)
    last_name = Column(String(20), nullable=False, index=True)
    phone = Column(String(20), nullable=False)
    role = Column(String(10), nullable=False, index=True)
    is_active = Column(Boolean, nullable=False)
    is_verified = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    uploated_at = Column(DateTime, default=datetime.now)

    accounts = relationship('Account', back_populates='user')

    def __repr__(self):
        return f"User<id={self.id}, first_name={self.first_name}, second_name={self.second_name}, last_name={self.last_name}>"
