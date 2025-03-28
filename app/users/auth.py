import os
from dotenv import load_dotenv

from app.users.dao import UserDAO

load_dotenv()

from passlib.context import CryptContext

from jose import jwt
from datetime import datetime, timedelta, timezone

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encode_jwt

async def authentificate_user(username: str, password: str):
    user = await UserDAO.find_one_or_none_by_username(username=username)
    if not user or verify_password(plain_password=password, hashed_password=user.password) is False:
        return None
    return user
