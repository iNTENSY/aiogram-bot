import datetime
import uuid
from dataclasses import dataclass

from src.domain.core.entity import DomainEntity
from src.domain.core.value_objects import IntegerIDVO, StringVO, UuidVO, DatetimeVO


@dataclass
class Book(DomainEntity):
    id: IntegerIDVO
    title: StringVO
    file_path: StringVO
    author: StringVO
    added_by: UuidVO
    created_at: DatetimeVO

    @staticmethod
    def create(id: int, title: str, file_path: str, author: str, added_by: uuid.UUID) -> "Book":
        return Book(
            id=IntegerIDVO(id),
            title=StringVO(title),
            file_path=StringVO(file_path),
            author=StringVO(author),
            added_by=UuidVO(added_by),
            created_at=DatetimeVO(datetime.datetime.now())
        )
