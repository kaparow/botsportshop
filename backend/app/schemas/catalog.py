from decimal import Decimal

from app.schemas.common import ORMModel


class CategoryRead(ORMModel):
    id: int
    name: str
    slug: str


class ProductRead(ORMModel):
    id: int
    category_id: int
    name: str
    slug: str
    description: str
    price: Decimal
    image_url: str
    is_active: bool
