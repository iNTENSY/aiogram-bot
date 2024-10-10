import logging
import os.path
from dataclasses import dataclass
from os.path import dirname
from typing import Any


@dataclass(frozen=True)
class LoggerConfig:
    level: Any
    name: str
    filename: str
    max_bytes: int
    backup_count: int
    log_directory: str

    @staticmethod
    def create(
            level: Any,
            name: str,
            filename: str,
            max_bytes: int,
            backup_count: int,
            log_dir: str = None
    ) -> 'LoggerConfig':
        if log_dir is None:
            log_dir = os.path.join(dirname(dirname(dirname(dirname(dirname(dirname(__file__)))))), "logs")
        return LoggerConfig(level, name, filename, max_bytes, backup_count, log_dir)
