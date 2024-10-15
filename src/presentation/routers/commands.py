from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from dishka import FromDishka

from src.applications.contracts.default import DefaultAiogramRequest
from src.applications.use_cases.commands.contacts import HandleContactsUseCase
from src.applications.use_cases.commands.help import HandleHelpUseCase
from src.applications.use_cases.commands.start import HandleStartUseCase

router = Router(name="Commands Handler")


@router.message(Command(commands=["start"]))
async def handle_start(message: Message, state: FSMContext, interactor: FromDishka[HandleStartUseCase]) -> None:
    contract = DefaultAiogramRequest(message, state, user=message.from_user)
    response = await interactor(contract)
    await state.set_state(response.state)
    await message.answer(text=response.message, reply_markup=response.keyboard)


@router.message(Command(commands=["help"]))
async def handle_help(message: Message, state: FSMContext, interactor: FromDishka[HandleHelpUseCase]) -> None:
    contract = DefaultAiogramRequest(message, state, user=message.from_user)
    response = await interactor(contract)
    await state.set_state(response.state)
    await message.answer(text=response.message, reply_markup=response.keyboard)


@router.message(Command(commands=["contacts"]))
async def support_handler(message: Message, state: FSMContext, interactor: FromDishka[HandleContactsUseCase]) -> None:
    response = await interactor()
    await state.set_state(response.state)
    await message.answer(text=response.message, reply_markup=response.keyboard)
