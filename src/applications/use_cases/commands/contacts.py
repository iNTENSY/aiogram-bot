from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from decouple import config

from src.applications.contracts.default import DefaultAiogramResponse
from src.applications.interfaces.interactor import Interactor
from src.infrastructure.services.internal.keyboards.contacts import ContactsInlineButton
from src.infrastructure.services.internal.keyboards.factory import KeyboardCombiner


class HandleContactsUseCase(Interactor[None, DefaultAiogramResponse]):
    def __init__(self, combiner: KeyboardCombiner) -> None:
        self.__combiner = combiner

    async def __call__(self, request=None) -> DefaultAiogramResponse:
        keyboard = self.__get_keyboard()
        content = "Для более быстрого решения проблемы обратитесь к автору."
        return DefaultAiogramResponse(message=content, keyboard=keyboard)

    def __get_keyboard(self) -> InlineKeyboardMarkup:
        self.__combiner.builder = InlineKeyboardBuilder()
        keyboard_rules = [ContactsInlineButton(author_id=int(config("AUTHOR_ID")))]
        keyboard = self.__combiner.combine(keyboard_rules)
        return keyboard
