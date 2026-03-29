import { NavLink } from 'react-router-dom'

const links = [
  { to: '/', label: 'Главная' },
  { to: '/cart', label: 'Корзина' },
  { to: '/profile', label: 'Профиль' },
]

export const BottomNav = () => (
  <nav className="bottom-nav">
    {links.map((item) => (
      <NavLink key={item.to} to={item.to} className={({ isActive }) => (isActive ? 'active' : '')}>
        {item.label}
      </NavLink>
    ))}
  </nav>
)
