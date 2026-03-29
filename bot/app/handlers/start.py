from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.core.config import get_settings
from app.keyboards.main import main_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    settings = get_settings()
    first_name = message.from_user.first_name if message.from_user else "спортсмен"
    await message.answer(
        f"Привет, {first_name}! Добро пожаловать в Hyper Nutrition 💪\nОткрой магазин и собери корзину.",
        reply_markup=main_keyboard(settings.mini_app_url),
    )
