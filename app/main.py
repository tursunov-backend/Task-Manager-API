from fastapi import FastAPI

from app.database import engine, Base
from app.models import *
from app.routers.auth import router as auths_router
from app.routers.projects import router as projects_router
from app.routers.tasks import router as tasks_router
from app.routers.users import router as users_router


Base.metadata.create_all(engine)

app = FastAPI(title="TASK MANAGER API")

app.include_router(auths_router)
app.include_router(projects_router)
app.include_router(tasks_router)
app.include_router(users_router)
