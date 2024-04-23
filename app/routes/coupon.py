from math import ceil

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app.services.coupon import CouponService

coupon_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@coupon_router.get("/cplist", include_in_schema=False)
async def redirect_to_cplist():
    return RedirectResponse("/cplist/1")


# 전체 쿠폰 조회
@coupon_router.get('/cplist/{cpg}', response_class=HTMLResponse)
def cplist(req: Request, cpg: int):
    stpg = int((cpg - 1) / 10) * 10 + 1
    cplist, cnt = CouponService.select_cplist(cpg)
    allpage = ceil(cnt / 10)  # 총 페이지 수
    return templates.TemplateResponse('coupon_log.html',
                                      {'request': req, 'cplist': cplist, 'cnt': cnt, 'cpg': cpg,
                                       'stpg': stpg, 'allpage': allpage, 'basesurl': '/cplist/'})


# 쿠폰 날짜 검색 조회
@coupon_router.get('/cplist/{skey}', response_class=HTMLResponse)
def find(req: Request, skey: str):
    cplist = CouponService.find_select_list('%' + skey + '%')
    row = CouponService.find_select_list('%' + skey + '%').fetchone()
    return templates.TemplateResponse('coupon_log.html',
                                      {'request': req, 'cplist': cplist, 'skey': skey, 'row': row})


# 차량 조회 페이지
@coupon_router.get('/carlist', response_class=HTMLResponse)
def carlist(req: Request):
    carlist = CouponService.select_carlist()
    row = CouponService.select_carlist().fetchone()
    return templates.TemplateResponse('select_cars.html',
                                      {'request': req, 'carlist': carlist, 'row': row})


# 차량 검색 조회
@coupon_router.get('/carlist/{nokey}/{tmkey}', response_class=HTMLResponse)
def find(req: Request, nokey: str, tmkey: str):
    carlist = CouponService.find_carlist('%' + nokey + '%', '%' + tmkey + '%')
    row = CouponService.find_carlist('%' + nokey + '%', '%' + tmkey + '%').fetchone()
    return templates.TemplateResponse('select_cars.html',
                                      {'request': req, 'carlist': carlist,
                                       'nokey': nokey, 'tmkey': tmkey, 'row': row})
