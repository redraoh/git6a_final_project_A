from datetime import datetime
from pydantic import BaseModel


class Member(BaseModel):
    mno: int
    mid: str
    mpwd: str
    mname: str
    pname: str
    regdate: datetime

    class Config:
        from_attributes = True
