from sqlalchemy import Column, String, Integer, SmallInteger
from werkzeug.security import generate_password_hash
from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(String(50), unique=True, nullable=False)
    email = Column(String(50))
    phone = Column(Integer)
    _password = Column('password', String(100))
    authority = Column(SmallInteger)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def add_user(account, secret):
        with db.auto_commit():
            temp = User()
            temp.account = account
            temp.password = secret
            db.session.add(temp)

    @classmethod
    def is_user_exist(cls, account):
        if User.query.filter_by(account=account).first():
            return True
        else:
            return False