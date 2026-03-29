import { useCartStore } from 'features/cart/store'
import type { Product } from 'shared/types'

export const ProductCard = ({ product }: { product: Product }) => {
  const addToCart = useCartStore((s) => s.addToCart)
  return (
    <article className="product-card">
      <img src={product.image_url} alt={product.name} />
      <div>
        <h3>{product.name}</h3>
        <p>{product.description}</p>
        <div className="product-footer">
          <strong>{Number(product.price).toLocaleString('ru-RU')} ₽</strong>
          <button onClick={() => addToCart(product.id)}>Добавить</button>
        </div>
      </div>
    </article>
  )
}
