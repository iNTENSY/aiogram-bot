from aiogram.filters.callback_data import CallbackData


class FinderBookCallbackFactory(CallbackData, prefix="finder"):
    previous: bool = False
    cancel: bool = False
    next: bool = False


class BookIDCallbackFactory(CallbackData, prefix="book"):
    book_id: int
