import math

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.exc import DBAPIError

from src.applications.contracts.books.requests import GetBooksRequest
from src.applications.contracts.default import DefaultAiogramResponse, PaginationResponse
from src.applications.interfaces.interactor import Interactor
from src.applications.interfaces.logger import ILogger
from src.domain.books.entity import Book
from src.domain.books.repository import IBookRepository
from src.infrastructure.services.internal.keyboards.actions import ActionsInlineKeyboard
from src.infrastructure.services.internal.keyboards.all_books import BooksInlineKeyboard
from src.infrastructure.services.internal.keyboards.factory import KeyboardCombiner
from src.infrastructure.settings.books import BooksSettings


class GetLimitedBooksUseCase(Interactor[GetBooksRequest, DefaultAiogramResponse]):
    def __init__(
            self,
            logger: ILogger,
            repository: IBookRepository,
            combiner: KeyboardCombiner,
            book_settings: BooksSettings
    ) -> None:
        self.__logger = logger
        self.__repository = repository
        self.__combiner = combiner
        self.__bk_settings = book_settings

    async def __call__(self, request: GetBooksRequest) -> PaginationResponse:
        books, page = await self.__get_books(request)
        keyboard = self.__get_keyboard(page, books)
        return PaginationResponse(
            message=f"[{page}] Список доступных книг:",
            state=None,
            keyboard=keyboard,
            page=page
        )

    async def __get_books(self, request: GetBooksRequest) -> tuple[list[Book], int]:
        page = request.page
        offset = self.__bk_settings.limit * (page - 1)
        books = await self.__repository.find_all(limit=self.__bk_settings.limit, offset=offset)
        if not books:
            page = 1
            offset = self.__bk_settings.limit * (page - 1)
            books = await self.__repository.find_all(limit=self.__bk_settings.limit, offset=offset)
        return books, page

    def __get_keyboard(self, page: int, books: list[Book]) -> InlineKeyboardMarkup:
        self.__combiner.builder = InlineKeyboardBuilder()
        keyboard_rules = [BooksInlineKeyboard(books), ActionsInlineKeyboard(page)]
        return self.__combiner.combine(keyboard_rules)
