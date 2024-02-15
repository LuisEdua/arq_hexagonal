from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

DATABASE_URI = 'mysql+mysqlconnector://root:RcBaR_-315@localhost/BDAH'

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)
