import { create } from 'zustand'
import { api } from 'shared/api/client'
import type { Order } from 'shared/types'

type OrdersState = {
  orders: Order[]
  loading: boolean
  fetchOrders: () => Promise<void>
}

export const useOrdersStore = create<OrdersState>((set) => ({
  orders: [],
  loading: false,
  fetchOrders: async () => {
    set({ loading: true })
    const { data } = await api.get<Order[]>('/orders')
    set({ orders: data, loading: false })
  },
}))
