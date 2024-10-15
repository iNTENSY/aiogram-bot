import datetime
import logging

from decouple import config
from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from src.applications.interfaces.logger import ILogger
from src.applications.use_cases.books.all import GetLimitedBooksUseCase
from src.applications.use_cases.books.get import GetBookUseCase
from src.applications.use_cases.commands.contacts import HandleContactsUseCase
from src.applications.use_cases.commands.help import HandleHelpUseCase
from src.domain.books.repository import IBookRepository
from src.infrastructure.persistence.repositories.books import BookRepositoryImp
from src.infrastructure.services.internal.keyboards.factory import KeyboardCombiner
from src.infrastructure.services.internal.logger.config import LoggerConfig
from src.infrastructure.services.internal.logger.logger import LoggerImp
from src.applications.interfaces.transaction_manager import ITransactionContextManager
from src.applications.use_cases.commands.start import HandleStartUseCase
from src.infrastructure.persistence.transactions import PostgreSQLTransactionContextManagerImp
from src.infrastructure.settings.books import BooksSettings
from src.infrastructure.settings.database import DatabaseConfig


class SQLAlchemyProvider(Provider):
    """
    Поставщик с возможностями получения настроек для работы с SQLAlchemy

    Providers:
        - DatabaseConfig (Scope: APP): Возможность получить конфигурацию для работы с базой данных.
        - AsyncEngine (Scope: APP): Асинхронный engine для SQLAlchemy.
        - AsyncSession (Scope: REQUEST): Генерация новой сессии при обращении.
    """

    @provide(scope=Scope.APP, provides=DatabaseConfig)
    def provide_settings(self) -> DatabaseConfig:
        user = config("POSTGRES_USER")
        password = config("POSTGRES_PASSWORD")
        host = config("DB_HOST")
        port = config("DB_PORT")
        db_name = config("POSTGRES_DB")
        return DatabaseConfig.create(user=user, password=password, host=host, port=port, database_name=db_name)

    @provide(scope=Scope.APP, provides=AsyncEngine)
    def provide_engine(self, settings: DatabaseConfig) -> AsyncEngine:
        return create_async_engine(settings.url)

    @provide(scope=Scope.APP, provides=async_sessionmaker[AsyncSession])
    def provide_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(self, session_maker: async_sessionmaker[AsyncSession]) -> AsyncSession:
        async with session_maker() as session:
            yield session


class TransactionManagerProvider(Provider):
    """
    Поставщик транзакций в базе данных

    Scope: REQUEST

    Providers:
        - ITransactionContextManager: Открытие транзакции при каждом обращении.
        (Стандартное поведение использует реализацию для PostgreSQL)
    """

    scope = Scope.REQUEST
    postgresql_manager = provide(PostgreSQLTransactionContextManagerImp, provides=ITransactionContextManager)


class HandlersProvider(Provider):
    """
    Поставщик сценариев использования.

    Scope: REQUEST

    Providers:
        - HandleStartUseCase: Обработчик сценария с командой /start
        - HandleHelpUseCase: Обработчик сценария с командой /help
    """
    scope = Scope.REQUEST

    start_handler = provide(HandleStartUseCase)
    help_handler = provide(HandleHelpUseCase)
    contacts_handler = provide(HandleContactsUseCase)
    books_handler = provide(GetLimitedBooksUseCase)
    get_book = provide(GetBookUseCase)


class LoggerProvider(Provider):
    """
    Поставщик объекта для ведения журнала (логирования) событий в ходе выполнения программы.

    Scope: APP

    Providers:
        - LoggerConfig: Конфигурация для журнала событий
        - ILogger: Объект для ведения журнала событий
    """
    @provide(scope=Scope.APP, provides=LoggerConfig)
    def provide_settings(self) -> LoggerConfig:
        level = logging.INFO
        name = "service-logger"
        filename = f"aiogram-bot.logs"
        max_bytes = 10 * 1024 * 1024  # 10 Mb
        backup_count = 5
        return LoggerConfig.create(level=level,
                                   name=name,
                                   filename=filename,
                                   max_bytes=max_bytes,
                                   backup_count=backup_count)

    @provide(scope=Scope.APP, provides=ILogger)
    def provide_logger(self, settings: LoggerConfig) -> ILogger:
        return LoggerImp(settings)


class RepositoriesProvider(Provider):
    scope = Scope.REQUEST
    books = provide(BookRepositoryImp, provides=IBookRepository)


class UtilityProvider(Provider):
    @provide(scope=Scope.REQUEST, provides=KeyboardCombiner)
    def provide_keyboard_combiner(self) -> KeyboardCombiner:
        return KeyboardCombiner()

    @provide(scope=Scope.APP, provides=BooksSettings)
    def provide_books_settings(self) -> BooksSettings:
        return BooksSettings(limit=2)
