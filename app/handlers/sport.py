from aiogram import Router, F
from app.keyboards import *

router_sport = Router()


@router_sport.callback_query(F.data == "sport")
async def sport(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("Добрый день! Это бот компании «Специальный технологический центр». \n\nОзнакомиться с основной "
            "информацией о компании можно по ссылке на нашем сайте (https://www.stc-spb.ru/). Рекомендуем "
            "подписаться на наш телеграм-канал (https://t.me/stc_vesti ), там можно узнать свежие новости "
            "предприятия. \n\nС дополнительной информацией можете ознакомиться через меню."),
        reply_markup=get_sport_keyboard())


@router_sport.callback_query(F.data == "sportkomp")
async def sportkomp(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("После полгода работы сотрудник может компенсировать 50% от стоимости абонемента, но не более 20 тыс. "
            "рублей."), reply_markup=get_back_sport())


@router_sport.callback_query(F.data == "korsport")
async def korsport(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("Мы поддерживаем корпоративный спорт: постоянно играем в волейбол, футбол, большой и настольный теннис. "
            "Также участвуем в квизах и внешних спортивных мероприятиях. Расписание можно посмотреть на портале СТЦ."),
        reply_markup=get_back_sport())