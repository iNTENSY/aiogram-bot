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
            "/help - Справочный центр бота.\n\n"
            "Все книги были найдены в открытых источниках, поэтому бот не несет ответственность"
            "за нарушение каких-либо запретов или законов.\n\n"
            "<b>Приятного чтения!</b>"
        )
        return DefaultAiogramResponse(message=content, state=None, keyboard=ReplyKeyboardRemove())
