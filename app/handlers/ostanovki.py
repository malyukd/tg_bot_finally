from aiogram import Router, F
from app.keyboards import *
from app.images import spots

router_ostanovki = Router()


@router_ostanovki.callback_query(F.data == "abobus")
async def ostanovki(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("Места посадок на автобус:"), reply_markup=get_ostanovki_keyboard())

@router_ostanovki.callback_query(F.data == "ostanovka_over")
async def ostanovka_over(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        str("Места посадок на автобус:"), reply_markup=get_ostanovki_keyboard())


@router_ostanovki.callback_query(F.data == "o1")
async def o1(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(spots[0], reply_markup=get_ostanovka_back_keyboard())


@router_ostanovki.callback_query(F.data == "o2")
async def o2(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(spots[1], reply_markup=get_ostanovka_back_keyboard())


@router_ostanovki.callback_query(F.data == "o3")
async def o3(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(spots[2], reply_markup=get_ostanovka_back_keyboard())


@router_ostanovki.callback_query(F.data == "o4")
async def o4(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(spots[3], reply_markup=get_ostanovka_back_keyboard())


@router_ostanovki.callback_query(F.data == "o5")
async def o5(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(spots[4], reply_markup=get_ostanovka_back_keyboard())

