from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from resources.resources import my_orders_at_work, my_orders_completed, my_orders_delayed


def admin_orders_completed_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=my_orders_completed())
    kb.button(text=my_orders_at_work())
    kb.button(text=my_orders_delayed())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
