from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


def get_main_keyboard():
    main_keyboard = [
        [
            types.InlineKeyboardButton(text="Документы для первого рабочего дня", callback_data="documents")
        ],
        [
            types.InlineKeyboardButton(text="Добровольное медицинское страхование (ДМС)", callback_data="dms")],
        [
            types.InlineKeyboardButton(text="Информация о развозке", callback_data="razvozka"),
            types.InlineKeyboardButton(text="Спорт", callback_data="sport"),
        ],
        [
            types.InlineKeyboardButton(text="Финансы", callback_data="money"),
            types.InlineKeyboardButton(text="Обучение", callback_data="study"),
        ]
    ]
    keybord_main = types.InlineKeyboardMarkup(inline_keyboard=main_keyboard)
    return keybord_main


def get_back_keyboard():
    back_keyboard = [
        [types.InlineKeyboardButton(text="Назад", callback_data="start")]
    ]
    keybord_back = types.InlineKeyboardMarkup(inline_keyboard=back_keyboard)
    return keybord_back


def get_sport_keyboard():
    sport_keyboard = [
        [
            types.InlineKeyboardButton(text="Корпоративный спорт", callback_data="korsport")
        ],
        [
            types.InlineKeyboardButton(text="Компенсация занятий спортом", callback_data="sportkomp")
        ],
        [
            types.InlineKeyboardButton(text="Назад", callback_data="start")
        ]
    ]
    keybord_sport = types.InlineKeyboardMarkup(inline_keyboard=sport_keyboard)
    return keybord_sport


def get_razvozka_keyboard():
    razvozka_keyboard = [
        [
            types.InlineKeyboardButton(text="Расписание движения автобуса", callback_data="raspisanie")
        ],
        [
            types.InlineKeyboardButton(text="Места посадок на автобус", callback_data="abobus")
        ],
        [
            types.InlineKeyboardButton(text="Назад", callback_data="start")
        ]
    ]
    keybord_razvozka = types.InlineKeyboardMarkup(inline_keyboard=razvozka_keyboard)
    return keybord_razvozka


def get_raspisanie_keyboard():
    razvozka_keyboard = [
        [
            types.InlineKeyboardButton(text="к производственной площадке «Ручьи»", callback_data="r1")
        ],
        [
            types.InlineKeyboardButton(text="от производственной площадки «Ручьи»", callback_data="r2")
        ],
        [
            types.InlineKeyboardButton(text="к производственной площадке «Юлмарт»", callback_data="r3")
        ],
        [
            types.InlineKeyboardButton(text="от производственной площадки «Юлмарт»", callback_data="r4")
        ],
        [
            types.InlineKeyboardButton(text="Назад", callback_data="razvozka")
        ]
    ]
    keybord_razvozka = types.InlineKeyboardMarkup(inline_keyboard=razvozka_keyboard)
    return keybord_razvozka


def get_money_keyboard():
    money_keyboard = [
        [
            types.InlineKeyboardButton(text="Материальная помощь", callback_data="money1"),
            types.InlineKeyboardButton(text="Поддержка детей сотрудников", callback_data="money2")
        ],
        [
            types.InlineKeyboardButton(text="Дарение денежных средств", callback_data="money3"),
            types.InlineKeyboardButton(text="Релокационная программа ", callback_data="money4")
        ],
        [
            types.InlineKeyboardButton(text="Назад", callback_data="start")
        ]
    ]
    keybord_money = types.InlineKeyboardMarkup(inline_keyboard=money_keyboard)
    return keybord_money
