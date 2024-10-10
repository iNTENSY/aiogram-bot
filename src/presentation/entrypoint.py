import sys
from os.path import dirname

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config

sys.path.append(dirname(dirname(dirname(__file__))))

from src.infrastructure.di.core import init_di
from src.presentation.routers.commands import router as commands_router
from src.presentation.routers.books import router as books_router


def init_routers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(commands_router)
    dispatcher.include_router(books_router)


def entrypoint() -> tuple[Bot, Dispatcher]:
    bot = Bot(token=config("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dispatcher = Dispatcher()
    init_di(dispatcher)
    init_routers(dispatcher)
    return bot, dispatcher


if __name__ == '__main__':
    _bot, _dispatcher = entrypoint()
    try:
        _dispatcher.run_polling(_bot)
    except KeyboardInterrupt:
        pass
