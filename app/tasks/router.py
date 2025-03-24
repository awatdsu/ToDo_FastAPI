from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from app.tasks.schemas import TTask, TTaskResponse
from app.tasks.dao import TaskDao
from app.users.dependencies import get_current_user
from app.users.dao import UserDAO
from app.models import User
from app.error_schemas import SuccesfulResponse, ErrorResponse

router = APIRouter(prefix="/{username}/ToDos")

@router.get("/", summary="Список всех заметок", response_model=list[TTaskResponse])
async def get_user_tasks(username: str, current_user: User = Depends(get_current_user)):
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None or current_user.id != res.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    return await TaskDao.find_all(str(current_user.id))

@router.post("/createToDo", summary="Добавление новой заметки", responses={
    200: {"model": SuccesfulResponse},
    403: {"model" : ErrorResponse}
})
async def add_new_task(username: str, task_data: TTask, current_user: User = Depends(get_current_user)):
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None or current_user.id != res.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    await TaskDao.add_new_task(task_owner=current_user, title=task_data.title, description=task_data.description)
    return {"ok": True, "message": "Заметка успешно создана!", "detail":"Заметка успешно создана!"}

@router.delete("/{task_id}", summary="Удаление заметки", responses={
    200: {"model": SuccesfulResponse},
    403: {"model" : ErrorResponse}
})
async def delete_task(username: str, task_id: UUID, current_user: User = Depends(get_current_user)):
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None or current_user.id != res.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    await TaskDao.delete_task(task_owner=current_user, task_id=task_id)
    return {"detail":"Заметка успешно удалена!"}

@router.patch("/{task_id}", summary="Выполнение заметки")
async def complete_task(username: str, task_id: UUID, current_user: User = Depends(get_current_user)):
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None or current_user.id != res.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    await TaskDao.complete_task(task_owner=current_user, task_id=task_id)
    return {"detail":"Заметка успешно выполнена!"}


@router.get("/{task_id}", summary="Получить заметку", response_model=TTaskResponse)
async def get_single_user_task(username: str, task_id: UUID, current_user: User = Depends(get_current_user)):
    res = await UserDAO.find_one_or_none_by_username(username)
    if res is None or current_user.id != res.id:
        raise HTTPException(status_code=403, detail="Forbidden")
    return await TaskDao.get_single_task(task_owner=current_user, task_id=task_id)
    