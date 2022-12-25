from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models import mongodb
from app.models.book import BookModel

#Path(__file__).resolve()가 현재 파일의 경로
#즉 BASE_DIR은 현재 경로의 상위 경로, 이 경우 app 폴더
BASE_DIR = Path(__file__).resolve().parent

#싱글톤 패턴으로 생성
app = FastAPI()

#css 파일을 사용하기 위해 필요
# app.mount("/static", StaticFiles(directory="static"), name="static")

#템플릿 생성
#directory를 통해 html 파일 지정, uvicorn을 실행하는 경로와 관련있음
templates = Jinja2Templates(directory=BASE_DIR/"templates")

#Response 타입이 html, 기본적으로 json 타입
#index.html에 request와 id 변수에 값 지정
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    book = BookModel(keyword="파이썬", publisher="public", price=1200, image='me.png')
    print(await mongodb.engine.save(book)) #save 함수가 async함수 이므로 즉 코루틴 함수 이므로 await을 붙임
    return templates.TemplateResponse("./index.html", {"request": request, "title": "콜렉터"})

#q를 통해 검색어 받기
@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q:str):
    return templates.TemplateResponse("./index.html", {"request": request, "keyword": q})

# DB와 연결하고 서버가 끝날때 DB와 연결 해제
# app이 시작될때 함수 실행
@app.on_event("startup")
def on_app_start():
    """before app starts"""
    mongodb.connect()

# app이 종료될때 함수 실행
@app.on_event("shutdown")
def on_app_shutdown():
    """after app shutdown"""
    mongodb.close()