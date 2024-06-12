from aiogram import Router, F
from app.keyboards import *

router = Router()


@router.callback_query(F.data == "documents")
async def documents(callback: types.CallbackQuery):
    keyboard = get_back_keyboard()
    await callback.message.edit_text(str("Перечень оригиналов документов, которые необходимо будет принести нам для "
                                         "оформления в первый рабочий день:\n\n1. Трудовая книжка или справка о "
                                         "ведении электронной трудовой книжки (если вы на нее перешли).\n2. "
                                         "Паспорт.\n3. СНИЛС.\n4. ИНН.\n5. Документы об образовании.\n6. Военный "
                                         "билет.\n7. Свидетельство о браке/ рождении детей.\n8. Реквизиты зарплатной "
                                         "карты (если у вас СБЕРБАНК). Не обязательно. Оформить зарплатную карту "
                                         "можно и у нас.\n9. Справка 182н с предыдущего места работы (для оформления "
                                         "больничных).\n\nСправку 182н и справку о ведении электронной трудовой "
                                         "книжки вам должны выдать на предыдущем месте работы."), reply_markup=keyboard)


@router.callback_query(F.data == "dms")
async def dms(callback: types.CallbackQuery):
    keyboard = get_back_keyboard()
    await callback.message.edit_text(
        str("Услуги ДМС для работников оказывает страховая компания «Капитал-полис». Всем сотрудникам, прошедших "
            "испытательный срок, предоставляется ДМС. Также сотрудники компании могут увеличить пакет ДМС и/или "
            "подключить страхование родственников. "), reply_markup=keyboard)


@router.callback_query(F.data == "study")
async def study(callback: types.CallbackQuery):
    await callback.message.edit_text(
        str("СТЦ является заказчиком целевого обучения в лучших технических вузах РФ с последующим гарантированным "
            "трудоустройством в компании.\nПомимо целевого обучения оплачиваем конференции и курсы для повышения "
            "квалификации сотрудников."), reply_markup=get_back_keyboard())
