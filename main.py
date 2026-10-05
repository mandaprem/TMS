from fastapi import FastAPI
from src.utils.db import Base , engine
from src.tasks.models import taskModel
from src.tasks.routes import task_routes
from src.user.routes import user_routes

Base.metadata.create_all(engine)


app = FastAPI(title="This is tms")
app.include_router(task_routes)
app.include_router(user_routes)