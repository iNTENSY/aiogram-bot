from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.domain.books.entity import Book
from src.infrastructure.services.internal.callbacks.book import FinderBookCallbackFactory, BookIDCallbackFactory
from src.infrastructure.services.internal.keyboards.core import AbstractTelegramKeyboard


class AllBooksKeyboard(AbstractTelegramKeyboard):
    @staticmethod
    def generate_keyboard(*args, **kwargs) -> InlineKeyboardMarkup:
        data: list[Book] = kwargs.get("data", [])
        builder = InlineKeyboardBuilder()

        if data:
            for book in data:
                title = f"[{book.author.value}] {book.title.value}"
                callback = BookIDCallbackFactory(book_id=book.id.value).pack()
                button = InlineKeyboardButton(text=title, callback_data=callback)
                builder.row(button)

        builder.row(*[
            InlineKeyboardButton(text="<<", callback_data=FinderBookCallbackFactory(previous=True).pack()),
            InlineKeyboardButton(text="Cancel", callback_data=FinderBookCallbackFactory(cancel=True).pack()),
            InlineKeyboardButton(text=">>", callback_data=FinderBookCallbackFactory(next=True).pack())
        ])
        return builder.as_markup()
