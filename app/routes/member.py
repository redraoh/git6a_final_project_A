from fastapi import APIRouter, Request, Form

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.requests import Request
from starlette import status
from fastapi.templating import Jinja2Templates

from app.services.member import MemberService



member_router = APIRouter()
# jinja2 설정
templates = Jinja2Templates(directory='views/templates')


# 로그인 페이지
@member_router.get('/login', response_class=HTMLResponse)
def login(req: Request):
    return templates.TemplateResponse('login.html', {'request': req})

@member_router.post('/login', response_class=HTMLResponse)
def login(req: Request, userid: str = Form(), passwd: str = Form()):
    result = MemberService.check_login(userid, passwd)
    if result:
        # 세션처리 - 회원아이디를 세션에 등록
        req.session['m'] = result.mid
        # 리디렉션되는 위치 지정하기
        return RedirectResponse(url='/discount', status_code=status.HTTP_303_SEE_OTHER)
    else:
        return HTMLResponse("""
            <script>
                alert('로그인에 실패하였습니다. 아이디 혹은 비밀번호를 확인하세요.');
                window.location.href = '/login';
            </script>
        """)

@member_router.get('/logout')
def logout(req: Request):
    req.session.clear()     # 생성된 세션객체 제거
    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)