from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.dbfactory import db_startup
from app.routes.car import car_router
from app.routes.coupon import coupon_router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield # 비동기 처리가 가능하게끔 yield
#     db_startup()

app = FastAPI()

# 세션처리를 미들웨어 설정
app.add_middleware(SessionMiddleware, secret_key='050924duedate')

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
# app.mount('/static', StaticFiles(directory='views/static'), name='static')

# 외부 route 파일 불러오기
app.include_router(coupon_router)
app.include_router(car_router)

# 서버시작시 디비 생성
@app.on_event('startup')
async def on_startup():
    db_startup()


@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html',{'request': req})    # 파일명과 넘길 데이터


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)