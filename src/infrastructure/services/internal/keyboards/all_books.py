from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.domain.books.entity import Book
from src.infrastructure.services.internal.callbacks.book import BookIDCallbackFactory
from src.infrastructure.services.internal.keyboards.core import AbstractTelegramKeyboard


class BooksInlineKeyboard(AbstractTelegramKeyboard):
    def __init__(self, books: list[Book]) -> None:
        self.books = books

    def generate_keyboard(
            self,
            builder: InlineKeyboardBuilder, *args, **kwargs
    ) -> None:
        for book in self.books:
            title = f"[{book.author.value}] {book.title.value}"
            callback = BookIDCallbackFactory(book_id=book.id.value).pack()
            button = InlineKeyboardButton(text=title, callback_data=callback)
            builder.row(button)
