from src.applications.contracts.books.requests import GetBooksRequest
from src.applications.contracts.default import DefaultAiogramResponse
from src.applications.interfaces.interactor import Interactor
from src.applications.interfaces.logger import ILogger
from src.domain.books.repository import IBookRepository
from src.infrastructure.services.internal.keyboards.all_books import AllBooksKeyboard


class GetAllBooksUseCase(Interactor[GetBooksRequest, DefaultAiogramResponse]):
    def __init__(self, logger: ILogger, repository: IBookRepository) -> None:
        self.__logger = logger
        self.__repository = repository

    async def __call__(self, request: GetBooksRequest) -> DefaultAiogramResponse:
        books = await self.__repository.find_all(limit=request.limit, offset=request.offset)
        keyboard = AllBooksKeyboard.generate_keyboard(data=books)
        return DefaultAiogramResponse(message="Список доступных книг:",
                                      state=None,
                                      keyboard=keyboard)
