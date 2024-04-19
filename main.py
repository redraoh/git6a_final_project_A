from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from app.dbfactory import db_startup
from app.routes.car import car_router

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key='20240216103735')

templates = Jinja2Templates(directory='views/templates')

@app.on_event('startup')
async def on_startup():
    db_startup()

app.include_router(car_router)


@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app',reload=True)