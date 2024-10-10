from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.infrastructure.services.internal.callbacks.book import FinderBookCallbackFactory
from src.infrastructure.services.internal.keyboards.core import AbstractTelegramKeyboard


class ActionsInlineKeyboard(AbstractTelegramKeyboard):
    def __init__(self, page):
        self.page = page

    def generate_keyboard(
            self,
            builder: InlineKeyboardBuilder, *args, **kwargs
    ) -> None:
        buttons = [
            InlineKeyboardButton(text="Cancel", callback_data=FinderBookCallbackFactory(cancel=True, page=self.page).pack()),
            InlineKeyboardButton(text=">>", callback_data=FinderBookCallbackFactory(page=self.page + 1).pack())
        ]

        if self.page - 1 > 0:
            buttons.insert(0, InlineKeyboardButton(text="<<", callback_data=FinderBookCallbackFactory(page=self.page - 1).pack()))

        builder.row(*buttons)
