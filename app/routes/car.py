from fastapi import APIRouter, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.services.car import CarService

car_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@car_router.get('/cars/', response_class=HTMLResponse)
def get_car_info(cno: int):
    car_info = CarService.get_car_info_by_number(cno)
    if car_info is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return {
        "no": car_info.cno,
        "ent_time": car_info.ent_time,
        "ptime": car_info.ptime,
        "ent": car_info.ent
    }