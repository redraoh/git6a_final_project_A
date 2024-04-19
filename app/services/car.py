from app.models.car import Car
from app.dbfactory import Session
from sqlalchemy import select


class CarService():
    @classmethod
    def get_car_info_by_number(cls, db, cno):
        last_four_digits = cno[-4:]  # cno의 뒤에서 4자리 추출

        with db() as sess:
            car_info = sess.query(Car).filter(Car.cno.endswith(last_four_digits)).first()
            # cno의 뒷 4자리로 끝나는 데이터를 검색

        return car_info

    @classmethod
    def update_car_info(car_info):
        with Session() as sess:
            sess.merge(car_info)
            sess.commit()