import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F
from app.keyboards import *
from app.images import file_ids

router_start = Router()


@router_start.message(Command("start"))
async def start(message: types.Message):
    keyboard = get_main_keyboard()
    await message.answer(
        "Добрый день! Это бот компании «Специальный технологический центр». \n\nОзнакомиться с основной "
        "информацией о компании можно по ссылке на нашем сайте (https://www.stc-spb.ru/). Рекомендуем "
        "подписаться на наш телеграм-канал (https://t.me/stc_vesti ), там можно узнать свежие новости "
        "предприятия. \n\nС дополнительной информацией можете ознакомиться через меню.",
        reply_markup=keyboard
    )


@router_start.callback_query(F.data == "start")
async def start_over(callback: types.CallbackQuery):
    keyboard = get_main_keyboard()
    await callback.message.edit_text(
        str("Добрый день! Это бот компании «Специальный технологический центр». \n\nОзнакомиться с основной "
            "информацией о компании можно по ссылке на нашем сайте (https://www.stc-spb.ru/). Рекомендуем "
            "подписаться на наш телеграм-канал (https://t.me/stc_vesti ), там можно узнать свежие новости "
            "предприятия. \n\nС дополнительной информацией можете ознакомиться через меню."), reply_markup=keyboard)
