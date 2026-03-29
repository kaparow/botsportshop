from fastapi import Depends, Header, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User


def get_current_user(
    db: Session = Depends(get_db),
    x_telegram_id: int | None = Header(default=None),
) -> User:
    if not x_telegram_id:
        raise HTTPException(status_code=401, detail="Missing X-Telegram-Id header")
    user = db.execute(select(User).where(User.telegram_id == x_telegram_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=401, detail="User not authorized")
    return user
