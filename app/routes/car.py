from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request


car_router = APIRouter()



templates = Jinja2Templates(directory='views/templates')

# 차량 데이터 조회

@car_router.get('/cars', response_class=HTMLResponse)
def cars(req: Request):
    return templates.TemplateResponse('discount_car.html', {'request': req})