from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.services.coupon import CouponService

coupon_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


# 쿠폰 조회 페이지
# 전체 쿠폰 조회
@coupon_router.get('/coupon', response_class=HTMLResponse)
def cplist(req: Request):
    cplist = CouponService.select_cplist()
    row = CouponService.select_cplist().fetchone()
    return templates.TemplateResponse('coupon_log.html', {'request': req, 'cplist': cplist, 'row': row})

# 쿠폰 날짜 검색 조회
@coupon_router.get('/cplist/{skey}', response_class=HTMLResponse)
def find(req: Request, skey: str):
    cplist = CouponService.find_select_list('%' + skey + '%')
    print(cplist)
    row = CouponService.find_select_list('%' + skey + '%').fetchone()
    return templates.TemplateResponse('slct_cp.html',
                                      {'request': req, 'cplist': cplist, 'skey': skey, 'row': row})

# 차량 조회 페이지
@coupon_router.get('/search', response_class=HTMLResponse)
def carlist(req: Request):
    return templates.TemplateResponse('select_cars.html', {'request': req})


# 차량 조회 페이지 - router
# @coupon_router.get('/carlist', response_class=HTMLResponse)
# def carlist(req: Request):
#     carlist = CouponService.select_carlist()
#     return templates.TemplateResponse('slct_car.html', {'request': req, 'carlist': carlist})


# 쿠폰 사용 집계 페이지
@coupon_router.get('/log', response_class=HTMLResponse)
def carlist(req: Request):
    return templates.TemplateResponse('coupon_summary.html', {'request': req})