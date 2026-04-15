from datetime import datetime
from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectUpdate


def get_projects(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(Project)
        .filter(Project.author_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def create_project(db: Session, project_in: dict):
    project = Project(
        title=project_in["title"],
        description=project_in.get("description"),
        author_id=project_in["author_id"],
        created_at=datetime.utcnow(),
    )

    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def update_project(db: Session, project: Project, project_in: ProjectUpdate):
    update_data = project_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(project, field, value)

    db.commit()
    db.refresh(project)
    return project


def delete_project(db: Session, project: Project):
    db.delete(project)
    db.commit()
    return True
