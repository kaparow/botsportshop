from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Hyper Nutrition API"
    api_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg2://postgres:postgres@db:5432/hyper_nutrition"
    cors_origins: str = "http://localhost:5173"
    telegram_bot_token: str = ""
    telegram_auth_enabled: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def cors_origins_list(self) -> list[str]:
        return [item.strip() for item in self.cors_origins.split(",") if item.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
