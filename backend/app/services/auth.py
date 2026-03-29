from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import TelegramAuthRequest


def upsert_telegram_user(db: Session, payload: TelegramAuthRequest) -> User:
    user = db.execute(select(User).where(User.telegram_id == payload.telegram_id)).scalar_one_or_none()
    if user:
        user.username = payload.username
        user.first_name = payload.first_name
        user.last_name = payload.last_name
    else:
        user = User(
            telegram_id=payload.telegram_id,
            username=payload.username,
            first_name=payload.first_name,
            last_name=payload.last_name,
        )
        db.add(user)
    db.commit()
    db.refresh(user)
    return user
