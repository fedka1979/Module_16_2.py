from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {'message': "Главная страница"}

@app.get('/user/admin')
async def admin() -> dict:
    return {'message': "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def id_(user_id: float = Path(ge=1, le=100, description='Enter User ID', example='10')) -> dict:
    return {f"Вы вошли как пользователь №": {user_id}}

@app.get('/user/{username}/{age}')
async def news(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
               age: float = Path(ge=18, le=120, description='Enter id', example='24')) -> dict:
    return {f"Информация о пользователе."
            f"Имя": {username}, 'Возраст': {age}}