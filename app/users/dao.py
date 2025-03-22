from uuid import UUID
from sqlalchemy import select

from app.dao_base import BaseDao
from app.models import User
from app.database import session_maker



class UserDAO(BaseDao):
    model = User

    @classmethod
    async def find_one_or_none_by_username(cls, username: str):
        async with session_maker() as session:
            query = select(cls.model).filter_by(username=username)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none_by_id(cls, user_id: str):
        async with session_maker() as session:
            query = select(cls.model).filter_by(id=UUID(user_id))
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    @classmethod
    async def add_user(cls, **user_data: dict):
        async with session_maker() as session:
            async with session.begin():
                new_user = User(**user_data)
                session.add(new_user)
                await session.flush()
                new_user_id = new_user.id
                await session.commit()
                return new_user_id
