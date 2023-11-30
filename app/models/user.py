from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer, String
db = _SQLAlchemy()

class CC(db.Model):
    __tablename__ = 'uuu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer)





