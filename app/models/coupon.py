from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import Base


class Coupon(Base):
    __tablename__ = 'product'

    dno = Column(Integer, primary_key=True, autoincrement=True)
    cno = Column(String(10), nullable=False, unique=True)
    disc = Column(String(20), nullable=False)
    disc_time = Column(DateTime, default=datetime.now)
