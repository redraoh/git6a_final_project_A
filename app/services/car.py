from app.models.car import Car
from app.dbfactory import Session
from sqlalchemy.exc import SQLAlchemyError

class CarService():
    @classmethod
    def get_car_info_by_number(cls, cno):
        last_four_digits = cno[-4:]  # cno의 뒤에서 4자리 추출

        try:
            with Session() as sess:
                car_info = sess.query(Car).filter(Car.cno.endswith(last_four_digits)).first()
                # cno의 뒷 4자리로 끝나는 데이터를 검색
                return car_info
        except SQLAlchemyError as e:
            # 데이터베이스 작업 중 에러 발생 시 처리
            print("Error occurred while querying database:", e)
            return None

    @classmethod
    def apply_discount(cls, car_info, discount):
        try:
            with Session() as sess:
                car_info.disc = discount
                # 변경된 정보를 데이터베이스에 추가
                sess.merge(car_info)  # merge 사용하여 변경된 엔티티를 데이터베이스에 반영
                sess.commit()  # 세션을 커밋하여 변경 사항을 실제로 데이터베이스에 반영

                return car_info
        except SQLAlchemyError as e:
            # 데이터베이스 작업 중 에러 발생 시 처리
            print("Error occurred while updating database:", e)
            return None
