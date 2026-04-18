from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import engine, Base
from app.routers import auth, users, projects, tasks


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)
    print("Database connected")

    yield

    print(" App shutting down")


app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
    lifespan=lifespan,
)

API_PREFIX = "/api"

app.include_router(auth.router, prefix=API_PREFIX)
app.include_router(users.router, prefix=API_PREFIX)
app.include_router(projects.router, prefix=API_PREFIX)
app.include_router(tasks.router, prefix=API_PREFIX)


@app.get("/", tags=["Root"])
def root():
    return {"message": "API working "}
