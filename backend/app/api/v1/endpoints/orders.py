from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.order import OrderRead
from app.services.orders import get_user_order, list_user_orders

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("", response_model=list[OrderRead])
def get_orders(user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> list[OrderRead]:
    return [OrderRead.model_validate(order) for order in list_user_orders(db, user)]


@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> OrderRead:
    order = get_user_order(db, user, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderRead.model_validate(order)
