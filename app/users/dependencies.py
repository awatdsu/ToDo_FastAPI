import os
from dotenv import load_dotenv
from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError
from datetime import datetime, timezone
from app.users.dao import UserDAO

load_dotenv()

def get_token(request: Request):
    token = request.cookies.get('users_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token not found')
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=os.getenv("ALGORITHM"))
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Токен не валидный!') from exc
    
    expire = payload.get('exp')
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)

    if (not expire) or (expire_time < datetime.now(timezone.utc)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Токен истек')

    user_id = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Не найден ID пользователя')

    user = await UserDAO.find_one_or_none_by_id(str(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')

    return user