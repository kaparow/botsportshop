from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.models.catalog import Category, Product


def list_categories(db: Session) -> list[Category]:
    return db.execute(select(Category).order_by(Category.id)).scalars().all()


def list_products(db: Session, category: str | None = None, search: str | None = None) -> list[Product]:
    stmt: Select[tuple[Product]] = select(Product).where(Product.is_active.is_(True))
    if category:
        stmt = stmt.join(Category).where(Category.slug == category)
    if search:
        like = f"%{search.lower()}%"
        stmt = stmt.where(Product.name.ilike(like))
    return db.execute(stmt.order_by(Product.id)).scalars().all()


def get_product(db: Session, product_id: int) -> Product | None:
    return db.get(Product, product_id)
