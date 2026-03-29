import asyncio

from aiogram import Bot, Dispatcher

from app.core.config import get_settings
from app.handlers.start import router as start_router


async def main() -> None:
    settings = get_settings()
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
