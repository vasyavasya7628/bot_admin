from aiogram import Router, F
from aiogram.types import Message

from actions.admin.keyboards.admin_orders_kb import my_orders_kb
from resources.resources import my_orders

admin_orders_at_work_router = Router()


@admin_orders_at_work_router.message(F.text == my_orders())
async def get_admin_orders_at_work(message: Message):
    await message.answer(
        my_orders(),
        reply_markup=my_orders_kb()
    )
