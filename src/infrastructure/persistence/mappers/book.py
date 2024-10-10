import datetime

from src.domain.books.entity import Book
from src.domain.core.value_objects import IntegerIDVO, StringVO, UuidVO, DatetimeVO
from src.infrastructure.persistence.mappers.core import AbstractMapper


class BookMapper(AbstractMapper):
    @staticmethod
    def generate_to_entity(obj: dict, **inner_entities) -> Book:
        return Book(
            id=IntegerIDVO(obj["id"]),
            title=StringVO(obj["title"]),
            file_path=StringVO(obj["file_path"]),
            author=StringVO(obj["author"]),
            added_by=UuidVO(obj["added_by"]),
            created_at=DatetimeVO(obj["created_at"])
        )
