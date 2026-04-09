# from typing import Annotated

# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from jose import jwt, JWTError
# from sqlalchemy.orm import Session

# from app.database import get_db
# from app.models.user import User
# from app.crud.user import get_user
# from app.config import settings


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


# def get_current_user(
#     token: Annotated[str, Depends(oauth2_scheme)],
#     db: Annotated[Session, Depends(get_db)],
# ) -> User:

#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     try:
#         payload = jwt.decode(
#             token,
#             settings.SECRET_KEY,
#             algorithms=[settings.ALGORITHM],
#         )

#         user_id: str = payload.get("sub")

#         if user_id is None:
#             raise credentials_exception

#     except JWTError:
#         raise credentials_exception

#     user = get_user(db, int(user_id))

#     if user is None:
#         raise credentials_exception

#     return user


# def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)],
# ) -> User:
#     if not current_user.is_active:
#         raise HTTPException(
#             status_code=400,
#             detail="Inactive user",
#         )
#     return current_user
