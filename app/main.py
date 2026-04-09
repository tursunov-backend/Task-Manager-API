from fastapi import FastAPI

from app.database import engine, Base

from app.routers import auth, users, projects, tasks


app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)


app.include_router(auth.router, prefix="/api")
app.include_router(users.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "API working 🚀"}
