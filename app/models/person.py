from app.models import Base
from sqlalchemy import Column, SmallInteger, Integer, String

class person(Base):
    id = db.Column('user_id', Integer, primary_key=True)
    mobile = db.Column(String(20))

    def keys(self):
        return ['nickname', 'email']