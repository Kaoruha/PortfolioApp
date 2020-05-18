from datetime import datetime

from sqlalchemy import Column, String, Integer, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base, db


class Tag(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), default='-')
    author = Column(String(50))
    icon_url = Column(String(255))
    status = Column(SmallInteger, default=1)
    update_time = Column(String(30))

    @staticmethod
    def add_tag(name, description, author, icon_url='/'):
        with db.auto_commit():
            temp = Tag()
            temp.name = name
            temp.description = description
            temp.author = author
            temp.icon_url = icon_url
            temp.update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            db.session.add(temp)

    @classmethod
    def is_exist(cls, uid):
        if cls.query.filter_by(id=uid, status=1).first():
            return True
        else:
            return False

    @classmethod
    def is_tag_exist(cls, tag_id):
        if cls.query.filter_by(id=tag_id, status=1).first():
            return True
        else:
            return False
