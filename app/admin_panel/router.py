from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates

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