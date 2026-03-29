from datetime import datetime
from decimal import Decimal

from app.models.order import OrderStatus
from app.schemas.common import ORMModel


class OrderItemRead(ORMModel):
    id: int
    product_id: int
    product_name: str
    price: Decimal
    quantity: int


class OrderRead(ORMModel):
    id: int
    total_amount: Decimal
    status: OrderStatus
    created_at: datetime
    items: list[OrderItemRead]
