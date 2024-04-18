from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import Base


class Member(Base):
    __tablename__ = 'member'

    mno = Column(Integer, primary_key=True, autoincrement=True)
    mid = Column(String(18), nullable=False, unique=True)
    mpwd = Column(String(18), nullable=False)
    mname = Column(String(20), nullable=False)
    pname = Column(String(40), nullable=False)
    regdate = Column(DateTime, default=datetime.now)
