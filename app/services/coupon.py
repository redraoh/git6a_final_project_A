from sqlalchemy import select

from app.dbfactory import Session
from app.models.coupon import Coupon
from app.models.car import Car


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
            stmt = select(Car.cno, Car.ent_time, Car.ent, Car.disc) \
                .order_by(Car.pno) \
                .offset(0).limit(20)
            result = sess.execute(stmt)
        return result
