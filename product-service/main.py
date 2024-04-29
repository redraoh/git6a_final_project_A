from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import database as sess
import pymodels as pym
import sqlmodels as sqlm

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
    return {"message": "Hello World"}


@app.get("/products", response_model=list[pym.Product])
async def list_products(db:Session = Depends(get_db)):
    products = db.query(sqlm.Product).all()
    return [pym.Product.from_orm(p) for p in products]

@app.post("/products", response_model=pym.Product)
async def create_product(product: pym.ProductCreate, db:Session = Depends(get_db)):

    product = sqlm.Product(**product.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return pym.Product.from_orm(product)

if __name__ == '__main__':
    sess.create_tables()
    uvicorn.run('main:app', port=8000, reload=True)
