from sqlalchemy import select, func
from app.database import session_maker

class BaseDao:
    model = None
    @classmethod
    async def find_all_users(cls, **filter_by):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            users = await session.execute(query)
            return users.scalars().all()
        
    @classmethod
    async def count(cls):
        async with session_maker() as session:
            query = select(func.count()).select_from(cls.model)
            res = await session.execute(query)
            return res.scalar()