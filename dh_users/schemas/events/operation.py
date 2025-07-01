"""Модуль для моделей обработки и создания событий"""

__author__: str = "Старков Е.П."

from uuid import UUID
from dh_platform.patterns.message_bus import Event


class UserValidateEvent(Event):
    """
    Валидация при создании пользователя

    Attributes:
        login (str): Логин пользователя
        password (str): Пароль пользователя
        email (str): Email пользователя
    """

    login: str
    password: str
    email: str


class UserAddEvent(UserValidateEvent):
    """
    Добавление пользователя

    Attributes:
        user_id (int): Идентификатор пользователя
        role (int | None)Ж Идентификатор роли
    """

    user_id: int
    role: int | None


class UserDeleteEvent(Event):
    user_id: int
    user_uuid: UUID
    force_delete: bool
