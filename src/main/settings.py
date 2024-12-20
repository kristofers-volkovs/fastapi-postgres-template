import logging
from enum import Enum

from pydantic_settings import BaseSettings


class LoggingLevel(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"

    @staticmethod
    def default() -> "LoggingLevel":
        return LoggingLevel.INFO

    def to_logging_type(self) -> int:
        logging_map = {
            self.ERROR: logging.ERROR,
            self.WARNING: logging.WARNING,
            self.INFO: logging.INFO,
            self.DEBUG: logging.DEBUG,
        }
        return logging_map[self]


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    LOGGING_LEVEL: LoggingLevel = LoggingLevel.default()


settings: Settings = Settings()
