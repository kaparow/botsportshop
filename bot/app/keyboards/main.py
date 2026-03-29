from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo


def main_keyboard(webapp_url: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🛍 Магазин", web_app=WebAppInfo(url=webapp_url))]],
        resize_keyboard=True,
    )
