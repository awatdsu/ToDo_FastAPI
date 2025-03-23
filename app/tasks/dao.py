"""
find_all - поиск всех заметок/заметок пользователя
add_new_task - добавление новой заметки
delete_task - удаление заметки пользователя
"""
from uuid import UUID
from sqlalchemy import delete, select
from app.models import Task, User
from app.database import session_maker

class TaskDao():

    @classmethod
    async def find_all(cls, user_id: str | None = None):
        async with session_maker() as session:
            query = select(Task).filter_by(owner_id=UUID(user_id))
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def add_new_task(cls, task_owner: User, **task_data: dict):
        async with session_maker() as session:
            async with session.begin():
                new_task = Task(**task_data, owner_id=task_owner.id, owner=task_owner)
                session.add(new_task)
                await session.flush()
                new_task_id = new_task.id
                await session.commit()
                return new_task_id
            
    @classmethod
    async def delete_task(cls, task_owner: User, task_id: UUID):
        async with session_maker() as session:
            async with session.begin():
                query = select(Task).filter_by(id=task_id, owner=task_owner)
                result = await session.execute(query)
                task_to_delete = result.scalar_one_or_none()
                if not task_to_delete:
                    return None
                await session.execute(
                    delete(Task).filter_by(id=task_id)
                )
                await session.commit()
                return task_id
    
    @classmethod
    async def get_single_task(cls, task_owner: User, task_id: UUID):
        async with session_maker() as session:
            query = select(Task).filter_by(owner=task_owner, id=task_id)
            res = await session.execute(query)
            return res.scalar_one_or_none()