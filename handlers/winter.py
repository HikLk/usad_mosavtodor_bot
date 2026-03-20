from aiogram import Router, F
from aiogram.types import Message
from config import MAIN_SPREADSHEET_ID, SINGLE_SHEET_GID, BUTTON_FULL_REPORT, BUTTON_WORKERS_EXCEL
from utils.helpers import get_report_info

router = Router(name="winter")

@router.message(F.text == BUTTON_FULL_REPORT)
async def send_full_report(message: Message):
    base_name, report_text = get_report_info()
    await message.answer(report_text)
    # Excel всей таблицы
    url = f"https://docs.google.com/spreadsheets/d/{MAIN_SPREADSHEET_ID}/export?format=xlsx"
    try:
        r = requests.get(url, timeout=40)
        r.raise_for_status()
        await message.answer_document(BufferedInputFile(r.content, f"{base_name}.xlsx"))
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить Excel: {e}")
        return
    # PDF
    pdf_url = f"https://docs.google.com/spreadsheets/d/{MAIN_SPREADSHEET_ID}/export?format=pdf&gid={SINGLE_SHEET_GID}&size=A3&portrait=false&fitw=true&gridlines=false&printtitle=false&sheetnames=false&fzr=false"
    try:
        r = requests.get(pdf_url, timeout=30)
        r.raise_for_status()
        await message.answer_document(BufferedInputFile(r.content, f"{base_name}.pdf"))
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить PDF: {e}")

@router.message(F.text == BUTTON_WORKERS_EXCEL)
async def send_workers_excel(message: Message):
    filename = "Данные по дорожным рабочим.xlsx"
    url = f"https://docs.google.com/spreadsheets/d/{MAIN_SPREADSHEET_ID}/export?format=xlsx&gid={SINGLE_SHEET_GID}"
    try:
        r = requests.get(url, timeout=40)
        r.raise_for_status()
        await message.answer_document(BufferedInputFile(r.content, filename))
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить данные по рабочим: {e}")