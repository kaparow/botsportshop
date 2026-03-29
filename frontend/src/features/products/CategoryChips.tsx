import { useProductStore } from './store'

export const CategoryChips = () => {
  const { categories, selectedCategory, setCategory } = useProductStore()
  return (
    <div className="chips">
      <button className={!selectedCategory ? 'chip active' : 'chip'} onClick={() => setCategory(null)}>Все</button>
      {categories.map((c) => (
        <button
          key={c.id}
          className={selectedCategory === c.slug ? 'chip active' : 'chip'}
          onClick={() => setCategory(c.slug)}
        >
          {c.name}
        </button>
      ))}
    </div>
  )
}
