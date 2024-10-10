from src.applications.contracts.books.requests import GetBookByIDRequest
from src.applications.contracts.books.responses import BookResponse
from src.applications.interfaces.interactor import Interactor
from src.applications.interfaces.logger import ILogger
from src.domain.books.repository import IBookRepository


class GetBookUseCase(Interactor[GetBookByIDRequest, BookResponse]):
    def __init__(self, logger: ILogger, repository: IBookRepository) -> None:
        self.__logger = logger
        self.__repository = repository

    async def __call__(self, request: GetBookByIDRequest) -> BookResponse:
        book = await self.__repository.filter_by(id=request.id)
        if not book:
            ...  # Must be exception
        return BookResponse.create(book[0])
