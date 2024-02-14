from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    cellphone = Column(String(13), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    activation_token = Column(String(255))
    verified_at = Column(DateTime)

DATABASE_URI = 'mysql+mysqlconnector://user:password@localhost/dbname'

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas basadas en los modelos definidos
def crear():
    Base.metadata.create_all(bind=engine)
