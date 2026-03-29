from decimal import Decimal

from pydantic import BaseModel

from app.schemas.common import ORMModel


class CartItemWrite(BaseModel):
    product_id: int
    quantity: int = 1


class CartItemUpdate(BaseModel):
    quantity: int


class CartItemRead(ORMModel):
    id: int
    product_id: int
    quantity: int
    product_name: str
    product_price: Decimal
    product_image_url: str


class CartRead(ORMModel):
    id: int
    items: list[CartItemRead]
    total_amount: Decimal
