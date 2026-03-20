from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import BUTTON_BACK, BUTTON_SUMMER_REPORT
from keyboards.main import get_main_keyboard, get_summer_keyboard

router = Router(name="common")

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Выберите нужный отчёт:\n\n"
        "❄️ — полный отчёт зимний\n"
        "🧑‍🏭 — данные по дорожным рабочим\n"
        "📋 — планы от РУАД\n"
        "🌞 — отчет по летним видам работ\n"
        "📊 — выполнения подрядчиков",
        #"😏 — посмотреть на Андрея",
        reply_markup=get_main_keyboard()
    )

@router.message(F.text == BUTTON_BACK)
async def back_to_main(message: Message):
    await message.answer("Возвращаемся в главное меню", reply_markup=get_main_keyboard())

@router.message(F.text == BUTTON_SUMMER_REPORT)
async def summer_menu(message: Message):
    await message.answer(
        "Выберите тип отчёта по летним видам работ:",
        reply_markup=get_summer_keyboard()
    )