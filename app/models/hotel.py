from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer, String
from app.models.base import Base
class Hotel(Base):
    __tablename__ = 'hotel'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Integer)
    location = Column(String(100))
    description = Column(String(600))
    src = Column(String(100))
    comments = Column(String(1000))