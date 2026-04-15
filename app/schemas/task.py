from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date

from app.models.enums import TaskStatus, TaskPriority


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

    status: TaskStatus = TaskStatus.PENDING
    priority: TaskPriority = TaskPriority.MEDIUM

    due_date: Optional[date] = None


class TaskCreate(TaskBase):
    project_id: int
    assignee_id: Optional[int] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None

    due_date: Optional[date] = None
    assignee_id: Optional[int] = None


class TaskResponse(TaskBase):
    id: int
    project_id: int
    assignee_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)
