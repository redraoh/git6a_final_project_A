from app.models.car import Car


class CarService():
    @staticmethod
    def get_car_info_by_number(cno):
        car_info = Car.query.filter(Car.cno == cno).first()
        return car_info