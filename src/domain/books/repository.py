from typing import Protocol

from src.domain.books.entity import Book


class IBookRepository(Protocol):
    async def create(self, entity: Book) -> None:
        raise NotImplementedError

    async def find_all(self, limit: int = 10, offset: int = 0) -> list[Book]:
        raise NotImplementedError

    async def filter_by(self, **parameters) -> list[Book]:
        raise NotImplementedError

    async def update(self, entity: Book) -> None:
        raise NotImplementedError

    async def delete(self, **parameters) -> None:
        raise NotImplementedError

    async def get_last_id(self) -> int:
        raise NotImplementedError

    async def count(self) -> int:
        raise NotImplementedError
