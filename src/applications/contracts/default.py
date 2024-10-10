from dataclasses import dataclass

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import Message, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, User


@dataclass(frozen=True)
class DefaultAiogramRequest:
    message: Message | None = None
    state: FSMContext | None = None
    keyboard: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | None = None
    user: User | None = None


@dataclass(frozen=True)
class DefaultAiogramResponse:
    message: str | None = None
    state: State | None = None
    keyboard: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | None = None
