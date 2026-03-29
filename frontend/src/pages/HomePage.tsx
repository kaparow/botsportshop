import { useEffect } from 'react'

import { CategoryChips } from 'features/products/CategoryChips'
import { ProductCard } from 'features/products/ProductCard'
import { useProductStore } from 'features/products/store'

export const HomePage = () => {
  const { products, loading, search, setSearch, fetchCategories, fetchProducts, selectedCategory } = useProductStore()

  useEffect(() => {
    fetchCategories()
  }, [fetchCategories])

  useEffect(() => {
    fetchProducts()
  }, [fetchProducts, selectedCategory, search])

  return (
    <section>
      <h1>Hyper Nutrition</h1>
      <input
        className="search"
        placeholder="Поиск товаров"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      <CategoryChips />
      {loading && <p>Загрузка...</p>}
      {!loading && products.length === 0 && <p className="empty">Товары не найдены.</p>}
      <div className="products-grid">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </section>
  )
}
