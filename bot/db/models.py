import datetime

from sqlalchemy import Integer, Column, VARCHAR, DateTime

from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    username = Column(VARCHAR(32), unique=False)
    reg_date = Column(DateTime, default=datetime.datetime.now())
    upp_date = Column(DateTime, default=datetime.datetime.now())

    def __str__(self):
        return f'<User:{self.user_id}>'
