from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import AuthResponse, TelegramAuthRequest
from app.services.auth import upsert_telegram_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/telegram", response_model=AuthResponse)
def auth_telegram(payload: TelegramAuthRequest, db: Session = Depends(get_db)) -> AuthResponse:
    user = upsert_telegram_user(db, payload)
    return AuthResponse.model_validate(user)
