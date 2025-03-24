from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates

from app.tasks.dao import TaskDao
from app.users.dao import UserDAO
from app.users.dependencies import get_current_user


router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/')
async def get_news_page(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request})

@router.get('/{username}/profile')
async def get_user_profile_html(username: str, request: Request, current_user=Depends(get_current_user)):
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None or current_user.id != res.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    tasks = await TaskDao.find_all(str(current_user.id))
    return templates.TemplateResponse(name='profile.html', context={'request': request, 'tasks': tasks})

@router.get('/{username}/profile/new-task')
async def create_new_task(username: str, request: Request, current_user=Depends(get_current_user)):
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None or current_user.id != res.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    return templates.TemplateResponse(name='create_task.html', context={'request': request})


@router.get('/auth/registration')
async def user_auth_reg(request: Request):
    return templates.TemplateResponse(name='registration.html', context={'request': request})

@router.get('/auth/login')
async def user_auth_login(request: Request):
    return templates.TemplateResponse(name='login.html', context={'request': request})
