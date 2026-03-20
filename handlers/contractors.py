from aiogram import Router, F
from aiogram.types import Message, BufferedInputFile
import requests

from config import CONTRACTORS_SPREADSHEET_ID, BUTTON_CONTRACTORS
from utils.helpers import get_msk_date_str

router = Router(name="contractors")


@router.message(F.text == BUTTON_CONTRACTORS)
async def send_contractors_excel(message: Message):
    today = get_msk_date_str()
    filename = f"Выполнения подрядчиков {today}.xlsx"

    url = f"https://docs.google.com/spreadsheets/d/{CONTRACTORS_SPREADSHEET_ID}/export?format=xlsx"

    await message.answer(f"📊 Выгружаю выполнения подрядчиков на {today}...")

    try:
        r = requests.get(url, timeout=40)
        r.raise_for_status()
        await message.answer_document(
            document=BufferedInputFile(file=r.content, filename=filename),
            caption="Полная таблица выполнений подрядчиков в Excel"
        )
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить таблицу подрядчиков: {str(e)}")