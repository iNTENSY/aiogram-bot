from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from src.infrastructure.services.internal.keyboards.core import AbstractTelegramKeyboard


class ContactsInlineButton(AbstractTelegramKeyboard):
    def __init__(self, author_id: int) -> None:
        self.author_id = author_id

    def generate_keyboard(
            self,
            builder: InlineKeyboardBuilder | ReplyKeyboardBuilder, *args, **kwargs
    ) -> None:
        button = InlineKeyboardButton(text="Написать автору бота", url=f'tg://user?id={self.author_id}')
        builder.row(button)
