"""Модуль для роутов"""

__author__: str = "Старков Е.П."

from fastapi import APIRouter

from dh_users.services import UserService

from . import schemas

user_routes: APIRouter = APIRouter(prefix="/users", tags=["users"])


@user_routes.post(
    "/register", response_model=schemas.UserDataOut,
    description="Регистрация нового пользователя в системе",
    tags=["users", "auth"]
)
async def register_user(data: schemas.UserRegister):
    """Регистрация пользователя"""
    return await UserService.create(data)


@user_routes.post("/current_delete", description="Удаление текущего пользователя")
async def delete_current_user():
    return await UserService.delete()


@user_routes.post("/delete", description="Удаление пользователя по uuid")
async def delete_user():
    return await UserService.delete()
