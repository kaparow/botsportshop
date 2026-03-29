from pydantic import BaseModel

from app.schemas.common import ORMModel


class TelegramAuthRequest(BaseModel):
    telegram_id: int
    username: str | None = None
    first_name: str
    last_name: str | None = None
    init_data: str | None = None


class AuthResponse(ORMModel):
    id: int
    telegram_id: int
    username: str | None
    first_name: str
    last_name: str | None
