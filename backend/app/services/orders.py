from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.order import Order
from app.models.user import User


def list_user_orders(db: Session, user: User) -> list[Order]:
    return (
        db.execute(
            select(Order)
            .options(joinedload(Order.items))
            .where(Order.user_id == user.id)
            .order_by(Order.created_at.desc())
        )
        .scalars()
        .unique()
        .all()
    )


def get_user_order(db: Session, user: User, order_id: int) -> Order | None:
    return (
        db.execute(
            select(Order)
            .options(joinedload(Order.items))
            .where(Order.user_id == user.id, Order.id == order_id)
        )
        .scalars()
        .first()
    )
