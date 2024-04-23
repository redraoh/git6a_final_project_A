from datetime import datetime

from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from app.schemas.car import Car
from app.services.car import CarService
from fastapi.responses import JSONResponse
car_router = APIRouter()



templates = Jinja2Templates(directory='views/templates')

# 차량 데이터 조회
@car_router.get('/discount', response_class=HTMLResponse)
def cars(request: Request):
    return templates.TemplateResponse('discount_car.html', {'request': request, 'cars': cars})


@car_router.get("/cars/{cno}", response_model=Car)
def get_car_info_by_number(cno: str):
    car_info = CarService.get_car_info_by_number(cno)
    if car_info:
        car_info.cno = str(car_info.cno)
        return car_info
    else:
        return JSONResponse(content={"error": "차량번호를 찾을 수 없습니다"}, status_code=404)
