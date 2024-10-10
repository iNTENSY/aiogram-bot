from aiogram import Dispatcher
from dishka import AsyncContainer, make_async_container
from dishka.integrations.aiogram import setup_dishka

from src.infrastructure.di.providers import (SQLAlchemyProvider,
                                             TransactionManagerProvider,
                                             HandlersProvider,
                                             LoggerProvider, RepositoriesProvider)


def ioc_factory() -> AsyncContainer:
    container = make_async_container(
        SQLAlchemyProvider(),
        TransactionManagerProvider(),
        HandlersProvider(),
        LoggerProvider(),
        RepositoriesProvider(),
    )
    return container


def init_di(dispatcher: Dispatcher) -> None:
    container = ioc_factory()
    setup_dishka(container, router=dispatcher, auto_inject=True)
