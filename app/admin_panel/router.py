from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from uuid import UUID
from app.tasks.dao import TaskDao
from app.users.dao import UserDAO
from app.users.dependencies import get_current_user


router = APIRouter(prefix="/admin",tags=['Админ-панель'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/')
async def get_admin_page(request: Request, current_user = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Forbidden")
    users = await UserDAO.find_all_users()
    users_count = await UserDAO.count()
    tasks_count = await TaskDao.count()
    return templates.TemplateResponse(name='admin.html', context={'request': request, 'users': users, "users_count": users_count, "tasks_count": tasks_count})

@router.get('/{user_id}/')
async def get_admin_user_page(request: Request, user_id: str, current_user = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Forbidden")
    tasks= await TaskDao.find_all(user_id=user_id)
    user = await UserDAO.find_one_or_none_by_id(user_id=user_id)
    return templates.TemplateResponse(name='admin_show_user.html', context={'request': request, 'tasks':tasks, 'user':user})

@router.get('/{user_id}/{task_id}')
async def get_admin_show_task(request: Request, user_id: str, task_id:str, current_user = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Forbidden")
    user = await UserDAO.find_one_or_none_by_id(user_id=user_id)
    task= await TaskDao.get_single_task(user, UUID(task_id))
    return templates.TemplateResponse(name='admin_show_task.html', context={'request': request, 'task':task, 'user':user})