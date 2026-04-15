from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.crud.task import (
    get_tasks,
    get_task,
    create_task,
    update_task,
    delete_task,
)
from app.dependencies import get_current_user


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=List[TaskResponse])
async def get_tasks_view(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
):
    return db.query(current_user.tasks).offset(skip).limit(limit).all()


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task_view(
    task_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    task = get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.assignee_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    return task


@router.post("/", response_model=TaskResponse)
async def create_task_view(
    task_in: TaskCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    data = task_in.model_dump()
    data["assignee_id"] = current_user.id

    return create_task(db, TaskCreate(**data))


@router.patch("/{task_id}", response_model=TaskResponse)
async def update_task_view(
    task_id: int,
    task_in: TaskUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    task = get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.assignee_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    return update_task(db, task, task_in)


@router.delete("/{task_id}")
async def delete_task_view(
    task_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    task = get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.assignee_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    delete_task(db, task)
    return {"detail": "Task deleted"}
