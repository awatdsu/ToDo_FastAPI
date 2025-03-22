import sys
import os

from fastapi import APIRouter, Depends
from app.users.rb import RBUser
from app.users.schemas import UUser
from app.users.dao import UserDAO

app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, app_dir)

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.get("/", summary="Получить всех пользователей", response_model=list[UUser])
async def get_all_users(request_body: RBUser = Depends()) -> list[UUser]:
    return await UserDAO.find_all_users(**request_body.to_dict())

@router.get("/{username}", summary="Получить одного пользователя по username")
async def get_user_by_username(username: str) -> UUser | dict:
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None:
        return {'message':f'Пользователь {username} не найден!'}
    return res
