from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from src.infrastructure.services.internal.keyboards.core import AbstractTelegramKeyboard


class KeyboardCombiner:
    def __init__(self) -> None:
        self.__builder = None

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, engine: ReplyKeyboardBuilder | InlineKeyboardBuilder):
        self.__builder = engine

    def combine(self, chain: list[AbstractTelegramKeyboard]) -> InlineKeyboardMarkup | ReplyKeyboardMarkup:
        for element in chain:
            element.generate_keyboard(self.__builder)
        return self.__builder.as_markup()
