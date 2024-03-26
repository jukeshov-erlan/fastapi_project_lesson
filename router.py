from fastapi import APIRouter, Depends
from typing import Annotated
from repository import STaskAdd, STaskGet, StaskId
from repository import TaskRepository


router = APIRouter(
    prefix="/tasks",
    tags = ["Таски"]

)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> StaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}



@router.get("") 
async def get_tasks() -> list[STaskGet]:
    tasks = await TaskRepository.get_all()
    return {"tasks": tasks}

