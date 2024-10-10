from aiogram.types import ReplyKeyboardRemove

from src.applications.contracts.default import DefaultAiogramRequest, DefaultAiogramResponse
from src.applications.interfaces.interactor import Interactor
from src.applications.interfaces.logger import ILogger


class HandleHelpUseCase(Interactor[DefaultAiogramRequest, DefaultAiogramResponse]):
    def __init__(self, logger: ILogger) -> None:
        self.__logger = logger

    async def __call__(self, request: DefaultAiogramRequest) -> DefaultAiogramResponse:
        self.__logger.info(
            f"Вызов /help пользователем: @{request.user.username} ({request.user.id}) "
            f"| Очистка состояния и удаление клавиатур"
        )

        content = (
            "<b>Бот для чтения книг</b>\n\n"
            "Доступные команды:\n\n"
            "/books - Список всех книг, присутствующих для чтения.\n"
            "/read {id:int} - Начать читать книгу под указанным ID.\n"
            "/reading - Получить список книг, которые вы читаете.\n"
            "/bookmarks - Получить список всех Ваших закладок в книге.\n"
            "/help - Справочный центр бота.\n\n"
            "Чтобы сохранить закладку в книге - нажмите на кнопку с номером страницы.\n\n"
            "<b>Приятного чтения!</b>"
        )
        return DefaultAiogramResponse(message=content, state=None, keyboard=ReplyKeyboardRemove())
