from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Numeric, Text
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from ..database import Base

class PaymentStatus(enum.Enum):
    DRAFT = "draft"             # Черновик (создан, но не отправлен)
    EXECUTED = "executed"       # Исполнен (деньги списаны)
    CANCELLED = "cancelled"     # Отменен пользователем

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)                               # Кто создал платеж
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)                         # Счет списания
    payment_request_id = Column(String(36), unique=True, index=True)                                # UUID клиента
    amount = Column(Numeric(10, 2), nullable=False)                                                 # Сумма платежа
    payee_name = Column(String(200), nullable=False)                                                # Название получателя (юр. лицо или ФИО)
    payee_account = Column(String(34), nullable=False)                                              # Счет получателя
    payee_bik = Column(String(9), nullable=False)                                                   # БИК банка
    payee_inn = Column(String(12), nullable=False)                                                  # ИНН
    purpose = Column(Text, nullable=False)                                                          # Назначение платежа (что оплачиваем)
    status = Column(Enum(PaymentStatus), nullable=False, index=True, default=PaymentStatus.DRAFT)   # Статус платежа
    created_at = Column(DateTime, default=datetime.now, index=True)                                 # Время создания                                 
    executed_at = Column(DateTime, nullable=True)                                                   # Время исполнения (когда статус стал EXECUTED)

    user = relationship("User", back_populates='payments')
    account = relationship("Account", back_populates='payments')

    def __repr__(self):
        return f"Payment<id={self.id}, account={self.account_id}, created={self.created_at}, amount={self.amount}, status={self.status}>"