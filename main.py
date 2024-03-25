import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from actions.admin.handlers.admin_district import admin_districts_router
from actions.admin.handlers.admin_reg_success import admin_reg_success_router
from actions.admin.handlers.admin_orders import admin_orders_router
from actions.admin.handlers.order_status import order_status_router_yes, order_status_router_no
from actions.orders.handlers.db_orders import order_info_router
from actions.orders.handlers.menu_districts import menu_district_router
from handlers.exceptions_catcher import exceptions_router
from handlers.start import start_router
from resources.resources import text_bot_token
import os
from dotenv import load_dotenv


# https://getemoji.com/
def get_bot():
    return


async def main():
    load_dotenv()

    bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(start_router,
                       admin_districts_router,
                       admin_reg_success_router,
                       order_status_router_yes,
                       order_status_router_no,
                       admin_orders_router,
                       menu_district_router,
                       order_info_router,
                       exceptions_router
                       )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    is_webhook_set = bot.get_webhook_info() is not None
    logging.info(is_webhook_set)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
