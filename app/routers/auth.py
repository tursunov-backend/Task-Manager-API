from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin, TokenResponse
from app.crud.user import get_user_by_username, create_user
from app.core.security import verify_password, create_access_token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserResponse)
async def register_view(
    user_in: UserCreate,
    db: Annotated[Session, Depends(get_db)],
):
    existing_user = get_user_by_username(db, user_in.username)

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    user = create_user(db, user_in)
    return user


@router.post("/login", response_model=TokenResponse)
async def login_view(
    user_in: UserLogin,
    db: Annotated[Session, Depends(get_db)],
):
    user = get_user_by_username(db, user_in.username)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})

    return TokenResponse(access_token=token, token_type="bearer")
