import asyncio
import logging
from app.handlers.handlers import router
from app.handlers.start import router_start
from app.handlers.razvozka import router_razvozka
from app.handlers.money import router_money
from app.handlers.sport import router_sport
from app.handlers.ostanovki import router_ostanovki
from config import TOKEN
from aiogram import Dispatcher
from aiogram import Bot

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    dp.include_router(router_start)
    dp.include_router(router_razvozka)
    dp.include_router(router_money)
    dp.include_router(router_sport)
    dp.include_router(router_ostanovki)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
