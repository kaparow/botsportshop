import { create } from 'zustand'
import { api } from 'shared/api/client'
import { getInitData, getTelegramUser } from 'shared/lib/telegram'
import type { User } from 'shared/types'

type AuthState = {
  user: User | null
  isReady: boolean
  initAuth: () => Promise<void>
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isReady: false,
  initAuth: async () => {
    const tgUser = getTelegramUser()
    if (!tgUser?.id) {
      set({ isReady: true })
      return
    }
    const { data } = await api.post<User>('/auth/telegram', {
      telegram_id: tgUser.id,
      username: tgUser.username,
      first_name: tgUser.first_name || 'Telegram',
      last_name: tgUser.last_name,
      init_data: getInitData(),
    })
    api.defaults.headers.common['X-Telegram-Id'] = String(data.telegram_id)
    set({ user: data, isReady: true })
  },
}))
