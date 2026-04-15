from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user_in: UserCreate):
    if get_user_by_username(db, user_in.username):
        raise HTTPException(status_code=400, detail="Username already taken")

    user = User(
        username=user_in.username,
        hashed_password=get_password_hash(user_in.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user: User, user_in: UserUpdate):
    update_data = user_in.model_dump(exclude_unset=True)

    if "username" in update_data:
        existing = get_user_by_username(db, update_data["username"])
        if existing and existing.id != user.id:
            raise HTTPException(status_code=400, detail="Username already taken")

    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data.pop("password"))

    for field, value in update_data.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
    return True
