from fastapi import APIRouter, Request, Form

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from fastapi.templating import Jinja2Templates

login_router = APIRouter()
# jinja2 설정
templates = Jinja2Templates(directory='views/templates')



# 로그인 페이지
@login_router.get('/login', response_class=HTMLResponse)
def login(req: Request):
    return templates.TemplateResponse('login.html', {'request': req})

