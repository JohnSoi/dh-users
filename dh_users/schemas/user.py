# pylint: disable=unnecessary-ellipsis
"""Модуль для схем данных"""

__author__: str = "Старков Е.П."

from datetime import date

from dh_access.schemas import AccessPublicData, AccessValidateData, RoleIdData
from dh_contacts.schemas import UserRegisterContactField
from dh_platform import schemas
from pydantic import BaseModel, Field, field_validator

from dh_users.exceptions import IncorrectDateOfBirth


class BaseUserData(BaseModel):
    """
    Базовые данные пользователя

    Attributes:
        surname (str): Фамилия
        name (str): Имя
        second_name (str | None): Отчество
        date_birthday (date): Дата рождения
    """

    surname: str = Field(..., min_length=2, max_length=50)
    name: str = Field(..., min_length=2, max_length=50)
    second_name: str | None = Field(..., min_length=2, max_length=50)
    date_birthday: date = Field(...)


class UserDataOut(
    BaseUserData,
    schemas.EntityID,
    schemas.EntityUUID,
    schemas.OperationDateTime,
    schemas.SoftDeletedDateTime,
):
    """Входные данные пользователя"""

    ...


class UserRegister(BaseUserData, AccessValidateData, UserRegisterContactField, RoleIdData):
    """Данные для регистрации"""

    @classmethod
    @field_validator("date_birthday")
    def validate_date_birthday(cls, value: date) -> date:
        """Валидатор даты рождения"""
        today = date.today()
        if value > today:
            raise IncorrectDateOfBirth("Дата рождения не может быть в будущем")

        # Дополнительная проверка на минимальный возраст (например 12 лет)
        min_age_date = date(today.year - 6, today.month, today.day)
        if value > min_age_date:
            raise IncorrectDateOfBirth("Пользователь должен быть старше 12 лет")

        return value

    class Config:
        """Конфиг"""

        json_encoders = {date: lambda v: v.strftime("%Y-%m-%d")}


__all__: list[str] = [
    "UserDataOut",
    "UserRegister",
]
