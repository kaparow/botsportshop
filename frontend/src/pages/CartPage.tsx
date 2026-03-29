import { useEffect } from 'react'

import { useCartStore } from 'features/cart/store'
import { useOrdersStore } from 'features/profile/orders-store'

export const CartPage = () => {
  const { cart, fetchCart, updateItem, deleteItem, checkout } = useCartStore()
  const fetchOrders = useOrdersStore((s) => s.fetchOrders)

  useEffect(() => {
    fetchCart()
  }, [fetchCart])

  const onCheckout = async () => {
    await checkout()
    await fetchOrders()
    alert('Заказ создан')
  }

  return (
    <section>
      <h1>Корзина</h1>
      {!cart?.items.length && <p className="empty">Корзина пока пустая.</p>}
      <div className="cart-list">
        {cart?.items.map((item) => (
          <div className="cart-item" key={item.id}>
            <img src={item.product_image_url} alt={item.product_name} />
            <div>
              <h4>{item.product_name}</h4>
              <p>{Number(item.product_price).toLocaleString('ru-RU')} ₽</p>
              <div className="qty-row">
                <button onClick={() => updateItem(item.id, item.quantity - 1)}>-</button>
                <span>{item.quantity}</span>
                <button onClick={() => updateItem(item.id, item.quantity + 1)}>+</button>
                <button className="danger" onClick={() => deleteItem(item.id)}>Удалить</button>
              </div>
            </div>
          </div>
        ))}
      </div>
      <footer className="checkout">
        <div>Итого: <strong>{Number(cart?.total_amount || 0).toLocaleString('ru-RU')} ₽</strong></div>
        <button disabled={!cart?.items.length} onClick={onCheckout}>Оформить заказ</button>
      </footer>
    </section>
  )
}
