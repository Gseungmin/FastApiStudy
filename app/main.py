from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("./index.html", {"request": request, "id": id})