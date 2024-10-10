from dataclasses import dataclass


@dataclass(frozen=True)
class DatabaseConfig:
    url: str

    @staticmethod
    def create(
            user: str,
            password: str,
            host: str,
            port: str | int,
            database_name: str,
            driver: str = "postgresql+asyncpg"
    ) -> "DatabaseConfig":
        """Фабричный метод для создания настроек связанных с подключением к базе данных."""

        connection_url = f"{driver}://{user}:{password}@{host}:{port}/{database_name}"
        return DatabaseConfig(url=connection_url)
