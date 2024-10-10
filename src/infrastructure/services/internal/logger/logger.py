import logging
import os.path
import sys
from logging.handlers import RotatingFileHandler

from src.applications.interfaces.logger import ILogger
from src.infrastructure.services.internal.logger.config import LoggerConfig


class LoggerImp(ILogger):
    def __init__(self, settings: LoggerConfig):
        self.__settings = settings
        self.__logger = logging.getLogger(settings.name)
        self.__set_config_to_logger()

    def __set_config_to_logger(self) -> None:
        filename = os.path.join(self.__settings.log_directory, self.__settings.filename)
        self.__logger.setLevel(self.__settings.level)
        file_handler = RotatingFileHandler(
            filename=filename,
            encoding='utf-8',
            maxBytes=self.__settings.max_bytes,
            backupCount=self.__settings.backup_count
        )
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)

    def debug(self, message: str) -> None:
        self.__logger.debug(message)

    def info(self, message: str) -> None:
        self.__logger.info(message)

    def warning(self, message: str) -> None:
        self.__logger.warning(message)

    def error(self, message: str) -> None:
        self.__logger.error(message)

    def critical(self, message: str) -> None:
        self.__logger.critical(message)
