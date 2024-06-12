import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F
from app.keyboards import *
from app.images import file_ids

router_money = Router()


@router_money.callback_query(F.data == "money")
async def money(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("Добрый день! Это бот компании «Специальный технологический центр». \n\nОзнакомиться с основной "
            "информацией о компании можно по ссылке на нашем сайте (https://www.stc-spb.ru/). Рекомендуем "
            "подписаться на наш телеграм-канал (https://t.me/stc_vesti ), там можно узнать свежие новости "
            "предприятия. \n\nС дополнительной информацией можете ознакомиться через меню."
            ), reply_markup=get_money_keyboard())


@router_money.callback_query(F.data == "money1")
async def money1(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("Материальная помощь предоставляется работнику: \n\n- При рождении / усыновлении ребенка /оформлении "
            "опекунства (единовременно, но не более 50 000 за каждого ребенка);\n- В связи со смертью члена (членов) "
            "его семьи (единовременно, но не более 35 000);\n- Родственникам работника в случае его смерти ("
            "единовременно, но не более 50 000);\n- В случае повреждения или утраты личного имущества в результате "
            "чрезвычайных обстоятельств (единовременно, не более 50 000);\n- В связи с заключением контракта с "
            "Министерством обороны России (единовременно, не более 250 000);\n- В случае заболевания (не более 500 "
            "000);\n- К ежегодному основному оплачиваемому отпуску (не более 10 000 в год, категория «рабочий»);\n- "
            "Для подготовки школьников в первый класс (не более 5 000).\n"), reply_markup=get_back_keyboard())


@router_money.callback_query(F.data == "money2")
async def money2(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("Предприятие поддерживает семьи сотрудников, в том числе и в вопросах детства. Работнику полагается: \n- "
            "Компенсация 50% стоимости путевки (но не более 10 000 в год на каждого ребенка) в детские "
            "санаторно-курортные, оздоровительные организации России для работников, чей стаж работы в СТЦ более 1 "
            "года, имеющих детей в возрасте от 6,5 до 15 лет;\n- Дополнительный оплачиваемый день отпуска 1 сентября "
            "для родителей первоклассника.\n"), reply_markup=get_back_keyboard())


@router_money.callback_query(F.data == "money3")
async def money3(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("Предоставляется в следующих случаях:\n- В связи с бракосочетанием (не более 35 000);\n- К юбилейной "
            "дате (не более 25 000, от 50 лет);\n- К 8 марта (не более 5 000)\n"), reply_markup=get_back_keyboard())


@router_money.callback_query(F.data == "money4")
async def money4(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("СТЦ поддерживает сотрудников, переехавших для работы на предприятии из регионов России. Выплачивается "
            "компенсация: \n- 100% стоимости транспортных расходов с территории проживания до расположения "
            "Предприятия (кроме бизнес-класса и СВ) сотруднику и членам х семей;\n- Частичной стоимости (не более 20 "
            "000 рублей) в течение 2 первых месяцев работы на Предприятии при условии заключения договора аренды "
            "жилья работником.\n"), reply_markup=get_back_keyboard())