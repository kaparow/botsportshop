import { create } from 'zustand'
import { api } from 'shared/api/client'
import type { Category, Product } from 'shared/types'

type ProductState = {
  categories: Category[]
  products: Product[]
  loading: boolean
  selectedCategory: string | null
  search: string
  fetchCategories: () => Promise<void>
  fetchProducts: () => Promise<void>
  setCategory: (slug: string | null) => void
  setSearch: (value: string) => void
}

export const useProductStore = create<ProductState>((set, get) => ({
  categories: [],
  products: [],
  loading: false,
  selectedCategory: null,
  search: '',
  fetchCategories: async () => {
    const { data } = await api.get<Category[]>('/categories')
    set({ categories: data })
  },
  fetchProducts: async () => {
    set({ loading: true })
    const { selectedCategory, search } = get()
    const { data } = await api.get<Product[]>('/products', {
      params: {
        category: selectedCategory || undefined,
        search: search || undefined,
      },
    })
    set({ products: data, loading: false })
  },
  setCategory: (slug) => set({ selectedCategory: slug }),
  setSearch: (value) => set({ search: value }),
}))
