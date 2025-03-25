import sys
import os

from fastapi import APIRouter, Depends, HTTPException, status
from app.models import User
from app.users.dependencies import get_current_user
# from app.users.rb import RBUser
from app.users.schemas import UUser
from app.users.dao import UserDAO
from app.tasks.router import router as task_router
from app.error_schemas import ErrorResponse

app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, app_dir)

router = APIRouter(
    prefix='/user',
    dependencies=[Depends(get_current_user)]
)

router.include_router(
    router = task_router
)

@router.get("/{username}", summary="Получить одного пользователя по username", responses={
    200: {"model": UUser},
    status.HTTP_403_FORBIDDEN: {"model" : ErrorResponse}
})
async def get_user_by_username(username: str, current_user : User = Depends(get_current_user)) -> UUser | dict:
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None:
        raise HTTPException(status_code=403, detail="Forbidden")
    if current_user.id != res.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    return res

@router.delete("/{username}", summary="Удалить пользователя по юзернейму", responses={
    200: {"model": UUser},
    status.HTTP_403_FORBIDDEN: {"model" : ErrorResponse}
})
async def delete_user_by_username(username: str, current_user: User = Depends(get_current_user)) -> UUser | dict:
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None:
        raise HTTPException(status_code=403, detail="Forbidden")
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Forbidden")
    await UserDAO.delete_user(str(res.id))
    return {"message": "User deleted successfully"}