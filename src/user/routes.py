from fastapi import APIRouter,Depends
from src.user import controllers
from src.user import dtos
from sqlalchemy.orm import Session
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register" ,response_model= dtos.userRersponseSchema)
def register(body:dtos.userSchema,db:Session = Depends(get_db)):
    return controllers.Register(body,db)


@user_routes.post("/login")
def login(body:dtos.loginSchema,db:Session = Depends(get_db)):
    return controllers.user_login(body,db)
