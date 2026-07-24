from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles # 얘도 node js랑 완전 똑같음
from fastapi.templating import Jinja2Templates  # <- node js의 템플릿엔진 (ejs) 이걸 서버 사이드 엔지니어링 sse?  일단 서버 사이드 렌더링임 진자가
# pip install Jinja2
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

app.mount("/static", StaticFiles(directory = "static"), name="static")
templates = Jinja2Templates(directory = "templates")

# HTML 페이지 제공
@app.get("/", response_class=HTMLResponse) # HTML 방식으로 반환할거란 얘기 그리고 데코레이터 때문에 아래 async 쪽 추가 기능임
async def get_page(request: Request): # async는 비동기
    return templates.TemplateResponse({"request": request}, "index.html")  # request객체를 딕셔너리로 반환

# 백엔드 API – JSON 데이터 제공
@app.get("/api/data")
async def get_data():
    return {"message": "FastAPI에서 보내는 데이터입니다"}


users = {
    0: {"userid": "apple", "name": "김사과"},
    1: {"userid": "banana", "name": "반하나"},
    2: {"userid": "orange", "name": "오렌지"}
}

# 사용자 조회
# http://127.0.0.1:8000/users/0 <- 배열 0번째
@app.get("/users/{id}")
def find_user(id: int):
    user = users.get(id)
    if user is None:
        return {"error": "해당 id 없음"}
    return user

# http://127.0.0.1:8000/users/0/userid  <- 배열 0번째의 userid
# http://127.0.0.1:8000/docs
@app.get("/users/{id}/{key}")
def find_user_by_key(id: int, key: str):
    user = users[id][key]
    return user



# 이름으로 사용자 조회
@app.get("/id-by-name")
def find_user_by_name(name: str):
    for idx, user in users.items():
        if user["name"] == name:
            return user
    return {"error": "데이터를 찾지 못함"}


# 사용자 생성
class User(BaseModel):
    userid: str
    name: str

@app.post("/users/{id}")
def create_user(id: int, user: User):
    if id in users:
        return {"error": "이미 존재하는 키"}
    users[id] = user.model_dump()
    return {"success": "ok"}
