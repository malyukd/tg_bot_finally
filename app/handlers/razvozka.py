from aiogram import Router, F
from app.keyboards import *
from app.images import file_ids

router_razvozka = Router()


@router_razvozka.callback_query(F.data == "razvozka")
async def razvozka(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("Добрый день! Это бот компании «Специальный технологический центр». \n\nОзнакомиться с основной "
            "информацией о компании можно по ссылке на нашем сайте (https://www.stc-spb.ru/). Рекомендуем "
            "подписаться на наш телеграм-канал (https://t.me/stc_vesti ), там можно узнать свежие новости "
            "предприятия. \n\nС дополнительной информацией можете ознакомиться через меню."),
        reply_markup=get_razvozka_keyboard())


@router_razvozka.callback_query(F.data == "raspisanie")
async def raspisanie(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("В случае возникновения вопросов, связанных с временем подачи автобусов, телефоны для связи с "
            "диспетчерами организации-перевозчика: \n📞Екатерина:  +7 (921) 868-68-88\n📞Виктор:  +7 (921) "
            "868-68-86\n\nВыберете интересующий вас маршрут:"), reply_markup=get_raspisanie_keyboard())


@router_razvozka.callback_query(F.data == "raspisanie_over")
async def raspisanie_over(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        str("В случае возникновения вопросов, связанных с временем подачи автобусов, телефоны для связи с "
            "диспетчерами организации-перевозчика: \n📞Екатерина:  +7 (921) 868-68-88\n📞Виктор:  +7 (921) "
            "868-68-86\n\nВыберете интересующий вас маршрут:"), reply_markup=get_raspisanie_keyboard())


@router_razvozka.callback_query(F.data == "r1")
async def r1(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(file_ids[0], reply_markup=get_raspisanie_back_keyboard())


@router_razvozka.callback_query(F.data == "r2")
async def r2(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(file_ids[1], reply_markup=get_raspisanie_back_keyboard())


@router_razvozka.callback_query(F.data == "r3")
async def r3(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(file_ids[2], reply_markup=get_raspisanie_back_keyboard())


@router_razvozka.callback_query(F.data == "r4")
async def r4(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(file_ids[3], reply_markup=get_raspisanie_back_keyboard())
