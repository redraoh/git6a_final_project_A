from sqlalchemy import select

from app.dbfactory import Session
from app.models.coupon import Coupon
from app.models.car import Board


class CouponService():
    @staticmethod
    def select_cplist():
        with Session() as sess:
            stmt = select(Coupon.dno, Coupon.cno, Coupon.disc, Coupon.disc_time) \
                .order_by(Coupon.dno) \
                .offset(0).limit(20)
            result = sess.execute(stmt)
        return result


    @staticmethod
    def select_carlist():
        with Session() as sess:
            stmt = select(Board.cno, Board.ent_time, Board.ent, Board.disc) \
                .order_by(Board.pno) \
                .offset(0).limit(20)
            result = sess.execute(stmt)
        return result
