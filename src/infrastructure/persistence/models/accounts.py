from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.persistence.models.core import BaseModel, uuidpk


class AccountModel(BaseModel):
    __tablename__ = "accounts"

    id: Mapped[uuidpk]
    username: Mapped[str]
    telegram_id: Mapped[int] = mapped_column(unique=True)
    phone: Mapped[str]
    is_verified: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
