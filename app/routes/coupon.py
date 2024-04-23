from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.services.coupon import CouponService

coupon_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


# 쿠폰 조회 페이지
@coupon_router.get('/coupon', response_class=HTMLResponse)
def cplist(req: Request):
    cplist = CouponService.select_cplist()
    row = CouponService.select_cplist().fetchone()
    return templates.TemplateResponse('coupon_log.html', {'request': req, 'cplist': cplist, 'row': row})


# 차량 조회 페이지
@coupon_router.get('/search', response_class=HTMLResponse)
def carlist(req: Request):
    return templates.TemplateResponse('select_cars.html', {'request': req})


# 차량 조회 페이지 - router
# @coupon_router.get('/carlist', response_class=HTMLResponse)
# def carlist(req: Request):
#     carlist = CouponService.select_carlist()
#     return templates.TemplateResponse('slct_car.html', {'request': req, 'carlist': carlist})
