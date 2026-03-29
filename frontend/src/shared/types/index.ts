export type Category = { id: number; name: string; slug: string }

export type Product = {
  id: number
  category_id: number
  name: string
  slug: string
  description: string
  price: string
  image_url: string
  is_active: boolean
}

export type CartItem = {
  id: number
  product_id: number
  quantity: number
  product_name: string
  product_price: string
  product_image_url: string
}

export type Cart = {
  id: number
  items: CartItem[]
  total_amount: string
}

export type OrderItem = {
  id: number
  product_id: number
  product_name: string
  price: string
  quantity: number
}

export type Order = {
  id: number
  total_amount: string
  status: 'new' | 'paid' | 'shipped' | 'completed' | 'cancelled'
  created_at: string
  items: OrderItem[]
}

export type User = {
  id: number
  telegram_id: number
  username: string | null
  first_name: string
  last_name: string | null
}
