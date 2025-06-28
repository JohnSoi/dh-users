"""Модуль для сервиса"""

__author__: str = "Старков Е.П."

from dh_platform.patterns.message_bus import message_bus
from dh_platform.services import BaseService

from dh_users.models import UserModel

from .schemas import events


class UserService(BaseService):
    """Сервис для работы с пользователями"""

    _MODEL = UserModel

    @classmethod
    async def _before_create(cls, create_data: dict) -> None:
        """Обработка перед созданием"""
        await message_bus.publish(events.UserValidateEvent(**create_data))

    @classmethod
    async def _after_create(cls, entity_data: UserModel) -> None:
        """Обработка после создания"""
        await message_bus.publish(events.UserAddEvent(**update_data.dict()))
