from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from resources.resources import text_admin_login


def get_kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=text_admin_login())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
