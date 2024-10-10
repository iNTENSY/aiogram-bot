from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.books.entity import Book
from src.domain.books.repository import IBookRepository
from src.infrastructure.persistence.mappers.book import BookMapper
from src.infrastructure.persistence.models import BookModel


class BookRepositoryImp(IBookRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def find_all(self, limit: int = 10, offset: int = 0) -> list[Book]:
        statement = select(BookModel).limit(limit).offset(offset)
        result = await self.__session.execute(statement)
        return [BookMapper.generate_to_entity(vars(book)) for book in result.scalars().all()]

    async def filter_by(self, **parameters) -> list[Book]:
        statement = select(BookModel).filter_by(**parameters)
        result = await self.__session.execute(statement)
        return [BookMapper.generate_to_entity(vars(book)) for book in result.scalars().all()]
