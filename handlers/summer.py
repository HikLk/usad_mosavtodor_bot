from aiogram import Router, F
from aiogram.types import Message, BufferedInputFile
import requests

from config import (
    SUMMER_SPREADSHEET_ID, DAILY_GID, CUM_GID,
    BUTTON_DAILY_SUMMER, BUTTON_CUM_SUMMER, BUTTON_FULL_SUMMER
)
from utils.helpers import get_msk_date_str
from keyboards.main import get_summer_keyboard

router = Router(name="summer")


@router.message(F.text == BUTTON_DAILY_SUMMER)
async def send_daily_summer(message: Message):
    today = get_msk_date_str()
    base_name = f"Данные за сутки {today}"
    excel_filename = f"{base_name}.xlsx"
    pdf_filename = f"{base_name}.pdf"

    await message.answer(f"📅 Выгружаю данные за сутки ({today})...")

    gid = DAILY_GID

    # Excel
    url = f"https://docs.google.com/spreadsheets/d/{SUMMER_SPREADSHEET_ID}/export?format=xlsx&gid={gid}"
    try:
        r = requests.get(url, timeout=40)
        r.raise_for_status()
        await message.answer_document(
            document=BufferedInputFile(file=r.content, filename=excel_filename),
            caption=None
        )
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить Excel (сутки): {str(e)}")
        return

    # PDF
    pdf_url = (
        f"https://docs.google.com/spreadsheets/d/{SUMMER_SPREADSHEET_ID}/export?"
        f"format=pdf&gid={gid}&size=A3&portrait=false&fitw=true&"
        f"gridlines=false&printtitle=false&sheetnames=false&fzr=false"
    )
    try:
        r = requests.get(pdf_url, timeout=30)
        r.raise_for_status()
        await message.answer_document(
            document=BufferedInputFile(file=r.content, filename=pdf_filename),
            caption=None
        )
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить PDF (сутки): {str(e)}")


@router.message(F.text == BUTTON_CUM_SUMMER)
async def send_cum_summer(message: Message):
    today = get_msk_date_str()
    base_name = f"Накопительные данные {today}"
    excel_filename = f"{base_name}.xlsx"
    pdf_filename = f"{base_name}.pdf"

    await message.answer(f"📊 Выгружаю накопительные данные ({today})...")

    gid = CUM_GID

    # Excel
    url = f"https://docs.google.com/spreadsheets/d/{SUMMER_SPREADSHEET_ID}/export?format=xlsx&gid={gid}"
    try:
        r = requests.get(url, timeout=40)
        r.raise_for_status()
        await message.answer_document(
            document=BufferedInputFile(file=r.content, filename=excel_filename),
            caption=None
        )
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить Excel (накопительные): {str(e)}")
        return

    # PDF
    pdf_url = (
        f"https://docs.google.com/spreadsheets/d/{SUMMER_SPREADSHEET_ID}/export?"
        f"format=pdf&gid={gid}&size=A3&portrait=false&fitw=true&"
        f"gridlines=false&printtitle=false&sheetnames=false&fzr=false"
    )
    try:
        r = requests.get(pdf_url, timeout=30)
        r.raise_for_status()
        await message.answer_document(
            document=BufferedInputFile(file=r.content, filename=pdf_filename),
            caption=None
        )
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить PDF (накопительные): {str(e)}")


@router.message(F.text == BUTTON_FULL_SUMMER)
async def send_full_summer(message: Message):
    today = get_msk_date_str()
    base_name = f"Отчет по летнему содержанию {today}"
    excel_filename = f"{base_name}.xlsx"

    await message.answer(f"📋 Выгружаю полный отчет по летнему содержанию ({today})...")

    # Excel — вся таблица
    url_excel = f"https://docs.google.com/spreadsheets/d/{SUMMER_SPREADSHEET_ID}/export?format=xlsx"
    try:
        r = requests.get(url_excel, timeout=40)
        r.raise_for_status()
        await message.answer_document(
            document=BufferedInputFile(file=r.content, filename=excel_filename),
            caption="Полная таблица (все листы) в Excel"
        )
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить Excel (полный): {str(e)}")
        return

    # PDF — данные за сутки
    pdf_filename_daily = f"{base_name} — сутки.pdf"
    pdf_url_daily = (
        f"https://docs.google.com/spreadsheets/d/{SUMMER_SPREADSHEET_ID}/export?"
        f"format=pdf&gid={DAILY_GID}&size=A3&portrait=false&fitw=true&"
        f"gridlines=false&printtitle=false&sheetnames=false&fzr=false"
    )
    try:
        r = requests.get(pdf_url_daily, timeout=30)
        r.raise_for_status()
        await message.answer_document(
            document=BufferedInputFile(file=r.content, filename=pdf_filename_daily),
            caption="Лист с данными за сутки"
        )
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить PDF (сутки): {str(e)}")

    # PDF — накопительные данные
    pdf_filename_cum = f"{base_name} — накопительные.pdf"
    pdf_url_cum = (
        f"https://docs.google.com/spreadsheets/d/{SUMMER_SPREADSHEET_ID}/export?"
        f"format=pdf&gid={CUM_GID}&size=A3&portrait=false&fitw=true&"
        f"gridlines=false&printtitle=false&sheetnames=false&fzr=false"
    )
    try:
        r = requests.get(pdf_url_cum, timeout=30)
        r.raise_for_status()
        await message.answer_document(
            document=BufferedInputFile(file=r.content, filename=pdf_filename_cum),
            caption="Лист с накопительными данными"
        )
    except Exception as e:
        await message.answer(f"❌ Не удалось выгрузить PDF (накопительные): {str(e)}")