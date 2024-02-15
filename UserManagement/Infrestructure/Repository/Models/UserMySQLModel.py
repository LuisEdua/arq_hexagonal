from sqlalchemy import Column, String, DateTime
from Database.MySQL import Base


class User(Base):
    __tablename__ = 'users'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    cellphone = Column(String(20), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    activation_token = Column(String(255))
    verified_at = Column(DateTime, nullable=True)
