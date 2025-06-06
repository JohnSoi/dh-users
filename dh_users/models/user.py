"""Модуль для модели пользователя"""

__author__: str = "Старков Е.П."

from datetime import datetime

from dh_platform.models import *
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class User(BaseModel, IDMixin, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    """
    Модель пользователя

    Examples:
        >>> user: User = User(id=1)
        >>> print(user.full_name) # ФИО пользователя
    """
    surname: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    second_name: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)

    date_birthday: Mapped[datetime] = mapped_column(DateTime(), nullable=False)

    @property
    def full_name(self) -> str:
        """ФИО"""
        return f"{self.surname} {self.name} {self.second_name}".strip()
