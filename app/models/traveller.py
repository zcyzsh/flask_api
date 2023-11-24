from app.libs.helper import is_isbn_or_key
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Float, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from math import floor
from app.libs.enums import PendingStatus
from app.libs.error_code import userError

class Traveller(UserMixin, Base):
    id = Column(Integer,primary_key=True)
    nickname = Column(String(24), nullable=False)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    def keys(self):
        return ['nickname', 'email']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    @staticmethod
    def verify(email, password):
        traveller = Traveller.query.filter_by(email=email).first()
        if not traveller:
            raise userError()
        if not traveller.check_password(password):
            raise userError()
        return {'uid': traveller.id}

