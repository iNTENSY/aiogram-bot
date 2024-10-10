from aiogram.filters.callback_data import CallbackData


class FinderBookCallbackFactory(CallbackData, prefix="finder"):
    cancel: bool = False
    page: int


class BookIDCallbackFactory(CallbackData, prefix="book"):
    book_id: int
