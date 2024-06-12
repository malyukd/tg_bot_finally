import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F

router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Добрый день! Это бот компании «Специальный технологический центр». \n\nОзнакомиться с основной "
        "информацией о компании можно по ссылке на нашем сайте (https://www.stc-spb.ru/). Рекомендуем "
        "подписаться на наш телеграм-канал (https://t.me/stc_vesti ), там можно узнать свежие новости "
        "предприятия. \n\nС дополнительной информацией можете ознакомиться через меню.",
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "documents")
async def documents(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(str("Перечень оригиналов документов, которые необходимо будет принести нам для "
                                         "оформления в первый рабочий день:\n\n1. Трудовая книжка или справка о "
                                         "ведении электронной трудовой книжки (если вы на нее перешли).\n2. "
                                         "Паспорт.\n3. СНИЛС.\n4. ИНН.\n5. Документы об образовании.\n6. Военный "
                                         "билет.\n7. Свидетельство о браке/ рождении детей.\n8. Реквизиты зарплатной "
                                         "карты (если у вас СБЕРБАНК). Не обязательно. Оформить зарплатную карту "
                                         "можно и у нас.\n9. Справка 182н с предыдущего места работы (для оформления "
                                         "больничных).\n\nСправку 182н и справку о ведении электронной трудовой "
                                         "книжки вам должны выдать на предыдущем месте работы."))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "dms")
async def dms(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("Услуги ДМС для работников оказывает страховая компания «Капитал-полис». Всем сотрудникам, прошедших "
            "испытательный срок, предоставляется ДМС. Также сотрудники компании могут увеличить пакет ДМС и/или "
            "подключить страхование родственников. "))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "razvozka")
async def razvozka(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("Добрый день! Это бот компании «Специальный технологический центр». \n\nОзнакомиться с основной "
            "информацией о компании можно по ссылке на нашем сайте (https://www.stc-spb.ru/). Рекомендуем "
            "подписаться на наш телеграм-канал (https://t.me/stc_vesti ), там можно узнать свежие новости "
            "предприятия. \n\nС дополнительной информацией можете ознакомиться через меню."))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "sport")
async def sport(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("Добрый день! Это бот компании «Специальный технологический центр». \n\nОзнакомиться с основной "
            "информацией о компании можно по ссылке на нашем сайте (https://www.stc-spb.ru/). Рекомендуем "
            "подписаться на наш телеграм-канал (https://t.me/stc_vesti ), там можно узнать свежие новости "
            "предприятия. \n\nС дополнительной информацией можете ознакомиться через меню."))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "sportkomp")
async def sportkomp(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("После полгода работы сотрудник может компенсировать 50% от стоимости абонемента, но не более 20 тыс. "
            "рублей."))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "korsport")
async def korsport(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("Мы поддерживаем корпоративный спорт: постоянно играем в волейбол, футбол, большой и настольный теннис. "
            "Также участвуем в квизах и внешних спортивных мероприятиях. Расписание можно посмотреть на портале СТЦ."))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "money")
async def money(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("Добрый день! Это бот компании «Специальный технологический центр». \n\nОзнакомиться с основной "
            "информацией о компании можно по ссылке на нашем сайте (https://www.stc-spb.ru/). Рекомендуем "
            "подписаться на наш телеграм-канал (https://t.me/stc_vesti ), там можно узнать свежие новости "
            "предприятия. \n\nС дополнительной информацией можете ознакомиться через меню."
            ))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "money1")
async def money1(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("Материальная помощь предоставляется работнику: \n\n- При рождении / усыновлении ребенка /оформлении "
            "опекунства (единовременно, но не более 50 000 за каждого ребенка);\n- В связи со смертью члена (членов) "
            "его семьи (единовременно, но не более 35 000);\n- Родственникам работника в случае его смерти ("
            "единовременно, но не более 50 000);\n- В случае повреждения или утраты личного имущества в результате "
            "чрезвычайных обстоятельств (единовременно, не более 50 000);\n- В связи с заключением контракта с "
            "Министерством обороны России (единовременно, не более 250 000);\n- В случае заболевания (не более 500 "
            "000);\n- К ежегодному основному оплачиваемому отпуску (не более 10 000 в год, категория «рабочий»);\n- "
            "Для подготовки школьников в первый класс (не более 5 000).\n"))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "money2")
async def money2(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("Предприятие поддерживает семьи сотрудников, в том числе и в вопросах детства. Работнику полагается: \n- "
            "Компенсация 50% стоимости путевки (но не более 10 000 в год на каждого ребенка) в детские "
            "санаторно-курортные, оздоровительные организации России для работников, чей стаж работы в СТЦ более 1 "
            "года, имеющих детей в возрасте от 6,5 до 15 лет;\n- Дополнительный оплачиваемый день отпуска 1 сентября "
            "для родителей первоклассника.\n"))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "money3")
async def money3(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("Предоставляется в следующих случаях:\n- В связи с бракосочетанием (не более 35 000);\n- К юбилейной "
            "дате (не более 25 000, от 50 лет);\n- К 8 марта (не более 5 000)\n"))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "money4")
async def money4(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("СТЦ поддерживает сотрудников, переехавших для работы на предприятии из регионов России. Выплачивается "
            "компенсация: \n- 100% стоимости транспортных расходов с территории проживания до расположения "
            "Предприятия (кроме бизнес-класса и СВ) сотруднику и членам х семей;\n- Частичной стоимости (не более 20 "
            "000 рублей) в течение 2 первых месяцев работы на Предприятии при условии заключения договора аренды "
            "жилья работником.\n"))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())


@router.callback_query(F.data == "study")
async def study(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await callback.message.edit_text(
        str("СТЦ является заказчиком целевого обучения в лучших технических вузах РФ с последующим гарантированным "
            "трудоустройством в компании.\nПомимо целевого обучения оплачиваем конференции и курсы для повышения "
            "квалификации сотрудников."))
    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())
