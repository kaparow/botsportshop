# Hyper Nutrition MVP

Полноценный MVP Telegram-экосистемы:
- Telegram Bot (aiogram 3)
- Backend API (FastAPI + SQLAlchemy 2 + Alembic + PostgreSQL)
- Telegram Mini App (React + Vite + TypeScript + Zustand)

## Архитектура
- **bot/** — отвечает только за коммуникацию в Telegram и открытие Mini App.
- **backend/** — единый API и бизнес-логика (каталог, корзина, заказы).
- **frontend/** — Mini App-клиент внутри Telegram WebApp.

## Быстрый запуск
1. `cp .env.example .env` и заполните `BOT_TOKEN`/`MINI_APP_URL`.
2. `docker compose up -d --build`
3. Применить миграции:
   ```bash
   docker compose exec backend alembic upgrade head
   ```
4. Засидить товары:
   ```bash
   docker compose exec backend python -m app.db.seed
   ```
5. API: http://localhost:8000/docs
6. Mini App: http://localhost:5173

## Локальная разработка без Docker (опционально)
### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
python -m app.db.seed
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Bot
```bash
cd bot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m app.main
```

## Безопасность Telegram initData
Сейчас MVP использует `POST /api/v1/auth/telegram` и доверяет данным клиента.
Для production добавьте серверную валидацию `initData` через HMAC SHA-256 (bot token) и проверку `auth_date`.

## Roadmap
- YooKassa / Telegram Payments
- Админка товаров и заказов
- Избранное
- Promo-коды
- Push/бот-уведомления
- Расширенные фильтры и сортировки


## Частые проблемы
- `ModuleNotFoundError: No module named 'app'` при `alembic upgrade head` внутри контейнера:
  - обновите контейнер backend после pull: `docker compose up -d --build backend`
  - затем повторите миграцию: `docker compose exec backend alembic upgrade head`
