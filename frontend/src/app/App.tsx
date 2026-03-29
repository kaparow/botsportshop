import { useEffect } from 'react'
import { Navigate, Route, Routes } from 'react-router-dom'

import { useAuthStore } from 'features/profile/store'
import { CartPage } from 'pages/CartPage'
import { HomePage } from 'pages/HomePage'
import { ProfilePage } from 'pages/ProfilePage'
import { BottomNav } from 'widgets/BottomNav'

export const App = () => {
  const { initAuth, isReady } = useAuthStore()

  useEffect(() => {
    initAuth()
  }, [initAuth])

  if (!isReady) return <main className="app-shell">Авторизация...</main>

  return (
    <main className="app-shell">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/cart" element={<CartPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
      <BottomNav />
    </main>
  )
}
