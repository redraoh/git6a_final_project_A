from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

import auth
import database as sess
import pymodels as pym
import sqlmodels as sqlm

# from fastapi.templating import Jinja2Templates
# templates = Jinja2Templates(directory='../msa-frontend')

# TailwindCSS
#app.mount("/static", StaticFiles(directory='views/static'), name='static')


app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:3000",  # 허용할 프론트엔드 도메인
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    #allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터베이스 세션 의존성 생성
def get_db():
    db = sess.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def index():
    return {"message": "not here"}

# @app.get("/users", response_model=list[pym.User])
# async def list_users(db:Session = Depends(get_db)):
#     users = db.query(sqlm.User).all()
#     return [pym.User.from_orm(p) for p in users]

# 회원가입 하기
@app.post("/users", response_model=pym.User)
async def create_user(user: pym.UserCreate, db:Session = Depends(get_db)):
    return auth.register(db, user)

# 로그인 하기
@app.post("/login", response_model=pym.Token)
async def login_user(user: pym.UserLogin, db:Session = Depends(get_db)):
    token = auth.authenticate(db, user)

    if not token:
        raise HTTPException(status_code=401, detail='로그인 실패!! - 아이디 혹은 비밀번호를 확인하세요')

    return token



if __name__ == '__main__':
    sess.create_tables()
    uvicorn.run('main:app', port=8020, reload=True)
