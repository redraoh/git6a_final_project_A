from sqlalchemy import select

from app.dbfactory import Session
from app.models.coupon import Coupon
from app.models.car import Car


class CouponService():
    @staticmethod
    def coupon_convert(cpto):
        data = cpto.model_dump()
        cp = Coupon(**data)
        data = {'dno': cp.dno, 'cno': cp.cno, 'disc': cp.disc,
                'disc_time': cp.disc_time}
        return data

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


    @staticmethod
    def find_select_list(skey):
        with Session() as sess:
            stmt = select(Coupon.dno, Coupon.cno, Coupon.disc, Coupon.disc_time)

            stmt = stmt.filter(Coupon.disc_time.like(skey)) \
                .order_by(Coupon.dno).offset(0).limit(20)
            result = sess.execute(stmt)

        return result