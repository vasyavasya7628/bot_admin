from aiogram import Router, F
from aiogram.types import Message

from actions.admin.keyboards.admin_orders_kb import admin_orders_kb
from resources.resources import my_orders

admin_orders_router = Router()


@admin_orders_router.message(F.text == my_orders())
async def check_admin_orders(message: Message):
    await message.answer(
        my_orders(),
        reply_markup=admin_orders_kb()
    )
