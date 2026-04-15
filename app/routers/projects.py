from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.crud.project import (
    get_projects,
    get_project,
    create_project,
    update_project,
    delete_project,
)
from app.dependencies import get_current_user


router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("/me", response_model=List[ProjectResponse])
async def get_projects_view(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
):
    return get_projects(db, user_id=current_user.id, skip=skip, limit=limit)


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project_view(
    project_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    project = get_project(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")

    return project


@router.post("/", response_model=ProjectResponse)
async def create_project_view(
    project_in: ProjectCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    data = project_in.model_dump()
    data["author_id"] = current_user.id
    return create_project(db, data)


@router.patch("/{project_id}", response_model=ProjectResponse)
async def update_project_view(
    project_id: int,
    project_in: ProjectUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    project = get_project(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")

    return update_project(db, project, project_in)


@router.delete("/{project_id}")
async def delete_project_view(
    project_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    project = get_project(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")

    delete_project(db, project)
    return {"detail": "Project deleted"}
