from aiogram.types import ReplyKeyboardRemove

from src.applications.interfaces.logger import ILogger
from src.applications.contracts.default import DefaultAiogramRequest, DefaultAiogramResponse
from src.applications.interfaces.interactor import Interactor


class HandleStartUseCase(Interactor[DefaultAiogramRequest, DefaultAiogramResponse]):
    def __init__(self, logger: ILogger) -> None:
        self.__logger = logger

    async def __call__(self, request: DefaultAiogramRequest) -> DefaultAiogramResponse:
        self.__logger.info(
            f"Вызов /start пользователем: @{request.user.username} ({request.user.id}) "
            f"| Очистка состояния и удаление клавиатур")

        content = (
            "<b>Привет, читатель!</b>\n\n"
            "Это бот, в котором ты можешь прочитать определенную книгу.\n\n"
            "Чтобы посмотреть список доступных команд - набери /help"
        )
        return DefaultAiogramResponse(message=content, state=None, keyboard=ReplyKeyboardRemove())
