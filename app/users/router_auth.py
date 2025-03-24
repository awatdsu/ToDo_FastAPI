from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.models import User
from app.users.auth import get_password_hash, authentificate_user, create_access_token
from app.users.dao import UserDAO
from app.users.dependencies import get_current_user
from app.users.schemas import SUserRegister, SUserAuth

router = APIRouter(prefix="/auth")


@router.post("/register")
async def register_user(user_data: SUserRegister) -> dict:
    user = await UserDAO.find_one_or_none_by_username(username=user_data.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь уже существует"
        )
    user_dict = user_data.model_dump()
    print(user_dict)
    user_dict['password'] = get_password_hash(user_data.password)
    await UserDAO.add_user(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}

@router.post("/login")
async def auth_user(response: Response, user_data: SUserAuth):
    check = await authentificate_user(username=user_data.username, password=user_data.password)
    if check is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Неверная почта или пароль'
            )
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'ok': True, 'access_token': access_token, 'refresh_token': None, 'message': 'Вы успешно вошли!'}

@router.get("/me")
async def get_me(user_data: User = Depends(get_current_user)):
    return {"ok": True, "user_data":user_data.username}

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {"message":"User logout successfully"}