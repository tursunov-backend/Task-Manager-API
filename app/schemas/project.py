from pydantic import BaseModel, ConfigDict
from typing import Optional


class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class ProjectResponse(ProjectBase):
    id: int
    author_id: int

    model_config = ConfigDict(from_attributes=True)
