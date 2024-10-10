import datetime
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.persistence.models.core import BaseModel, intpk


class BookModel(BaseModel):
    __tablename__ = "books"

    id: Mapped[intpk]
    title: Mapped[str]
    file_path: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    added_by: Mapped[uuid.UUID] = mapped_column(ForeignKey("accounts.id", ondelete="CASCADE"))
    created_at: Mapped[datetime.datetime]
