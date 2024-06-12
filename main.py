import asyncio
import logging
from app.handlers.handlers import router
from config import TOKEN
from aiogram import Dispatcher
from aiogram import Bot

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
