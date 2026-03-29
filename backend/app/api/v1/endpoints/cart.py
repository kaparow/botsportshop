from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.cart import CartItemUpdate, CartItemWrite, CartRead
from app.schemas.order import OrderRead
from app.services.cart import add_item, checkout, delete_item, get_cart_payload, update_item

router = APIRouter(prefix="/cart", tags=["cart"])


@router.get("", response_model=CartRead)
def get_cart(user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> CartRead:
    return get_cart_payload(db, user)


@router.post("/items", response_model=CartRead)
def create_cart_item(payload: CartItemWrite, user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> CartRead:
    return add_item(db, user, payload.product_id, payload.quantity)


@router.patch("/items/{item_id}", response_model=CartRead)
def patch_cart_item(item_id: int, payload: CartItemUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> CartRead:
    return update_item(db, user, item_id, payload.quantity)


@router.delete("/items/{item_id}", response_model=CartRead)
def remove_cart_item(item_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> CartRead:
    return delete_item(db, user, item_id)


@router.post("/checkout", response_model=OrderRead)
def checkout_cart(user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> OrderRead:
    order = checkout(db, user)
    return OrderRead.model_validate(order)
