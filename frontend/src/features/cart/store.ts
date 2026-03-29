import { create } from 'zustand'
import { api } from 'shared/api/client'
import type { Cart } from 'shared/types'

type CartState = {
  cart: Cart | null
  loading: boolean
  fetchCart: () => Promise<void>
  addToCart: (productId: number) => Promise<void>
  updateItem: (itemId: number, quantity: number) => Promise<void>
  deleteItem: (itemId: number) => Promise<void>
  checkout: () => Promise<void>
}

export const useCartStore = create<CartState>((set, get) => ({
  cart: null,
  loading: false,
  fetchCart: async () => {
    set({ loading: true })
    const { data } = await api.get<Cart>('/cart')
    set({ cart: data, loading: false })
  },
  addToCart: async (productId) => {
    const { data } = await api.post<Cart>('/cart/items', { product_id: productId, quantity: 1 })
    set({ cart: data })
  },
  updateItem: async (itemId, quantity) => {
    const { data } = await api.patch<Cart>(`/cart/items/${itemId}`, { quantity })
    set({ cart: data })
  },
  deleteItem: async (itemId) => {
    const { data } = await api.delete<Cart>(`/cart/items/${itemId}`)
    set({ cart: data })
  },
  checkout: async () => {
    await api.post('/cart/checkout')
    await get().fetchCart()
  },
}))
