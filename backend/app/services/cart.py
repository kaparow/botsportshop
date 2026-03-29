from decimal import Decimal

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.cart import Cart, CartItem
from app.models.catalog import Product
from app.models.order import Order, OrderItem, OrderStatus
from app.models.user import User
from app.schemas.cart import CartRead, CartItemRead


def get_or_create_cart(db: Session, user: User) -> Cart:
    cart = db.execute(select(Cart).where(Cart.user_id == user.id)).scalar_one_or_none()
    if not cart:
        cart = Cart(user_id=user.id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart


def build_cart_read(cart: Cart) -> CartRead:
    items: list[CartItemRead] = []
    total = Decimal("0")
    for item in cart.items:
        price = item.product.price
        subtotal = price * item.quantity
        total += subtotal
        items.append(
            CartItemRead(
                id=item.id,
                product_id=item.product_id,
                quantity=item.quantity,
                product_name=item.product.name,
                product_price=price,
                product_image_url=item.product.image_url,
            )
        )
    return CartRead(id=cart.id, items=items, total_amount=total)


def get_cart_payload(db: Session, user: User) -> CartRead:
    cart = get_or_create_cart(db, user)
    cart = (
        db.execute(
            select(Cart)
            .options(joinedload(Cart.items).joinedload(CartItem.product))
            .where(Cart.id == cart.id)
        )
        .scalars()
        .first()
    )
    return build_cart_read(cart)


def add_item(db: Session, user: User, product_id: int, quantity: int) -> CartRead:
    if quantity < 1:
        raise HTTPException(status_code=400, detail="Quantity must be >= 1")
    cart = get_or_create_cart(db, user)
    product = db.get(Product, product_id)
    if not product or not product.is_active:
        raise HTTPException(status_code=404, detail="Product not found")

    cart_item = db.execute(
        select(CartItem).where(CartItem.cart_id == cart.id, CartItem.product_id == product_id)
    ).scalar_one_or_none()
    if cart_item:
        cart_item.quantity += quantity
    else:
        db.add(CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity))
    db.commit()
    return get_cart_payload(db, user)


def update_item(db: Session, user: User, item_id: int, quantity: int) -> CartRead:
    cart = get_or_create_cart(db, user)
    item = db.execute(select(CartItem).where(CartItem.id == item_id, CartItem.cart_id == cart.id)).scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    if quantity <= 0:
        db.delete(item)
    else:
        item.quantity = quantity
    db.commit()
    return get_cart_payload(db, user)


def delete_item(db: Session, user: User, item_id: int) -> CartRead:
    cart = get_or_create_cart(db, user)
    item = db.execute(select(CartItem).where(CartItem.id == item_id, CartItem.cart_id == cart.id)).scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    db.delete(item)
    db.commit()
    return get_cart_payload(db, user)


def checkout(db: Session, user: User) -> Order:
    cart = get_or_create_cart(db, user)
    cart = (
        db.execute(
            select(Cart)
            .options(joinedload(Cart.items).joinedload(CartItem.product))
            .where(Cart.id == cart.id)
        )
        .scalars()
        .first()
    )
    if not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = sum((item.product.price * item.quantity for item in cart.items), Decimal("0"))
    order = Order(user_id=user.id, total_amount=total, status=OrderStatus.new)
    db.add(order)
    db.flush()

    for item in cart.items:
        db.add(
            OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                product_name=item.product.name,
                price=item.product.price,
                quantity=item.quantity,
            )
        )

    for item in list(cart.items):
        db.delete(item)

    db.commit()
    db.refresh(order)
    return order
