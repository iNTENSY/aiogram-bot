import asyncio
import random
from pprint import pprint

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile
from dishka import FromDishka

from src.applications.contracts.books.requests import GetBooksRequest, GetBookByIDRequest
from src.applications.use_cases.books.all import GetLimitedBooksUseCase
from src.applications.use_cases.books.get import GetBookUseCase
from src.infrastructure.services.internal.callbacks.book import FinderBookCallbackFactory, BookIDCallbackFactory


router = Router()


@router.message(Command(commands=["books"]))
async def handle_books(
        message: Message,
        state: FSMContext,
        interactor: FromDishka[GetLimitedBooksUseCase]
) -> None:
    await state.clear()
    response = await interactor(GetBooksRequest(page=1))
    await state.set_state(response.state)
    await message.answer(text=response.message, reply_markup=response.keyboard)


@router.callback_query(FinderBookCallbackFactory.filter(F.cancel))
async def handle_cancel_callback(callback: CallbackQuery) -> None:
    await callback.answer(text="Вы закрыли список всех книг")
    await asyncio.sleep(0.1)
    await callback.message.edit_text(text="** Список скрыт **", reply_markup=None)


@router.callback_query(BookIDCallbackFactory.filter())
async def handle_book_id(
        callback: CallbackQuery,
        callback_data: BookIDCallbackFactory,
        interactor: FromDishka[GetBookUseCase]
) -> None:
    contract = GetBookByIDRequest(id=callback_data.book_id)
    response = await interactor(contract)
    await callback.message.answer_document(FSInputFile(response.file_path), caption=response.title)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(FinderBookCallbackFactory.filter())
async def handle_action_callback(
        callback: CallbackQuery,
        callback_data: FinderBookCallbackFactory,
        interactor: FromDishka[GetLimitedBooksUseCase],
) -> None:
    contract = GetBooksRequest(page=callback_data.page)
    response = await interactor(contract)
    await callback.answer()
    await callback.message.edit_text(f"[{response.page}] Список доступных книг:")
    await callback.message.edit_reply_markup(reply_markup=response.keyboard)
