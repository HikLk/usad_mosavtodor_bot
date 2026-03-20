from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import (
    BUTTON_FULL_REPORT, BUTTON_WORKERS_EXCEL, BUTTON_PLANS_EXCEL,
    BUTTON_SUMMER_REPORT, BUTTON_CONTRACTORS, BUTTON_ANDREY,
    BUTTON_DAILY_SUMMER, BUTTON_CUM_SUMMER, BUTTON_FULL_SUMMER, BUTTON_BACK
)

def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BUTTON_FULL_REPORT)],
            [KeyboardButton(text=BUTTON_WORKERS_EXCEL)],
            [KeyboardButton(text=BUTTON_PLANS_EXCEL)],
            [KeyboardButton(text=BUTTON_SUMMER_REPORT)],
            [KeyboardButton(text=BUTTON_CONTRACTORS)],
            # [KeyboardButton(text=BUTTON_ANDREY)],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

def get_summer_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BUTTON_DAILY_SUMMER)],
            [KeyboardButton(text=BUTTON_CUM_SUMMER)],
            [KeyboardButton(text=BUTTON_FULL_SUMMER)],
            [KeyboardButton(text=BUTTON_BACK)],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )