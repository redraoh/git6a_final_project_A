from datetime import datetime
from pydantic import BaseModel


class Coupon(BaseModel):
    dno: int
    cno: str
    disc: str
    disc_time: datetime

    class Config:
        from_attributes = True