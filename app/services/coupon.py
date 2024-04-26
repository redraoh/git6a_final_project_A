from sqlalchemy import select, and_, func

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
    def car_convert(cto):
        data = cto.model_dump()
        car = Car(**data)
        data = {'pno': car.pno, 'cno': car.cno, 'pname': car.pname,
                'ent': car.ent, 'ent_time': car.ent_time, 'check': car.check,
                'exit_time': car.exit_time, 'ptime': car.ptime, 'disc': car.disc}
        return data

    # coupon list 조회
    @staticmethod
    def select_cplist(cpg):
        stnum = (cpg - 1) * 10

        with Session() as sess:
            cnt = sess.query(func.count(Coupon.dno)).scalar()

            stmt = select(Coupon.dno, Coupon.cno, Coupon.disc, Coupon.disc_time) \
                .order_by(Coupon.dno) \
                .offset(stnum).limit(10)
            result = sess.execute(stmt)
        return result, cnt

    # search coupon list 조회 - month, date
    @staticmethod
    def find_select_list(skey, cpg):
        stnum = (cpg - 1) * 10
        with Session() as sess:
            stmt = select(Coupon.dno, Coupon.cno, Coupon.disc, Coupon.disc_time)
            myfilter = Coupon.disc_time.like(skey)

            stmt = stmt.filter(myfilter) \
                .order_by(Coupon.dno).offset(stnum).limit(10)
            result = sess.execute(stmt)

            cnt = sess.query(func.count(Coupon.dno)) \
                .filter(myfilter).scalar()

        return result, cnt

    # car ent list 조회
    @staticmethod
    def select_carlist(cpg):
        stnum = (cpg - 1) * 10

        with Session() as sess:
            cnt = sess.query(func.count(Car.pno)).scalar()

            stmt = select(Car.cno, Car.ent_time, Car.ent, Car.disc) \
                .order_by(Car.pno) \
                .offset(stnum).limit(10)
            result = sess.execute(stmt)
        return result, cnt

    # search car ent list 조회 - cno && ent_time
    @staticmethod
    def find_carlist(nokey, tmkey, cpg):
        stnum = (cpg - 1) * 10
        with Session() as sess:
            stmt = select(Car.cno, Car.ent, Car.ent_time)
            myfilter = and_(Car.cno.like(nokey), Car.ent_time.like(tmkey))

            stmt = stmt.filter(myfilter) \
                .order_by(Car.pno).offset(stnum).limit(10)
            result = sess.execute(stmt)

            cnt = sess.query(func.count(Car.pno)) \
                .filter(myfilter).scalar()

        return result, cnt

    # coupon summary 검색 조회
    @staticmethod
    def find_cplist_summary(skey):

        with Session() as sess:
            # 검색필터
            myfilter = Coupon.disc_time.like(skey)

            # 기본 group by statement
            stmt = select(Coupon.dno, Coupon.cno, Coupon.disc, Coupon.disc_time
                          , func.count(Coupon.dno).label('count')) \
                .order_by(Coupon.dno).group_by(Coupon.disc)

            # srch table rowcount
            srchcnt = len(list(sess.execute(stmt.filter(myfilter))))

            # table rowcount
            wlcnt = len(list(sess.execute(stmt)))
            cnt = srchcnt + wlcnt
            print(f'총카운트 {srchcnt}+{wlcnt}={cnt}')

            schlist = sess.execute(stmt.filter(myfilter))
            wlist = sess.execute(stmt)

        return schlist, wlist, srchcnt, wlcnt, cnt
