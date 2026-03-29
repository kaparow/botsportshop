from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.catalog import list_categories
from app.schemas.catalog import CategoryRead

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("", response_model=list[CategoryRead])
def get_categories(db: Session = Depends(get_db)) -> list[CategoryRead]:
    categories = list_categories(db)
    return [CategoryRead.model_validate(item) for item in categories]
