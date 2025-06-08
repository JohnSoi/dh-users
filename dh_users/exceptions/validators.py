"""Модуль для исключения валидации"""

__author__: str = "Старков Е.П."

from dh_platform.exceptions import BaseAppException
from fastapi import status


class IncorrectDateOfBirth(BaseAppException):
    """Некорректная дата рождения"""

    _CODE = status.HTTP_422_UNPROCESSABLE_ENTITY
