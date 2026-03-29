import { useEffect } from 'react'

import { useAuthStore } from 'features/profile/store'
import { useOrdersStore } from 'features/profile/orders-store'

export const ProfilePage = () => {
  const { user } = useAuthStore()
  const { orders, fetchOrders, loading } = useOrdersStore()

  useEffect(() => {
    fetchOrders()
  }, [fetchOrders])

  return (
    <section>
      <h1>Профиль</h1>
      {user && (
        <div className="profile-box">
          <p><strong>Имя:</strong> {user.first_name} {user.last_name || ''}</p>
          <p><strong>Username:</strong> @{user.username || 'unknown'}</p>
          <p><strong>Telegram ID:</strong> {user.telegram_id}</p>
        </div>
      )}
      <h2>Мои заказы</h2>
      {loading && <p>Загрузка заказов...</p>}
      {!loading && orders.length === 0 && <p className="empty">Заказов пока нет.</p>}
      {orders.map((order) => (
        <article className="order-card" key={order.id}>
          <header>
            <strong>Заказ #{order.id}</strong>
            <span>{new Date(order.created_at).toLocaleString('ru-RU')}</span>
          </header>
          <p>Статус: <b>{order.status}</b></p>
          <ul>
            {order.items.map((item) => (
              <li key={item.id}>{item.product_name} × {item.quantity}</li>
            ))}
          </ul>
          <strong>{Number(order.total_amount).toLocaleString('ru-RU')} ₽</strong>
        </article>
      ))}
    </section>
  )
}
