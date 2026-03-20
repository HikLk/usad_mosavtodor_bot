import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# ID таблиц
MAIN_SPREADSHEET_ID = "1f248h28pbE16o9pKgvJuSbh2ViKAsfTE_OK3qIRP6TA"
SINGLE_SHEET_GID = "1841691264"
PLANS_SPREADSHEET_ID = "1SPmkft_ZvZr4tmCBcmzN0AE7HPscy3aRwB82uqR34CU"
CONTRACTORS_SPREADSHEET_ID = "1u7Hn4snGNAMNjMyXo7fcOUxS7vdzTS6Dj9n3J_IXVu0"
SUMMER_SPREADSHEET_ID = "14w0tzn5xsX2ZX5zgHYfEsMZ8p0ZX2f3rLhO_yR0I-3A"

DAILY_GID = "1539583525"
CUM_GID   = "1514416922"

MSK_OFFSET = timedelta(hours=3)

# Кнопки
BUTTON_FULL_REPORT    = "Отчет по зимним видам работ ❄️"
BUTTON_WORKERS_EXCEL  = "Количество дорожных рабочих для МТДИ 🧑‍🏭"
BUTTON_PLANS_EXCEL    = "Планы от РУАД 📋"
BUTTON_SUMMER_REPORT  = "Отчет по летним видам работ 🌞"
BUTTON_CONTRACTORS    = "Выполнения подрядчиков 📊"
# BUTTON_ANDREY         = "Посмотреть на Андрея 😏"   # временно убрано

BUTTON_DAILY_SUMMER   = "Выгрузить данные за сутки 📅"
BUTTON_CUM_SUMMER     = "Выгрузить накопительные данные 📊"
BUTTON_FULL_SUMMER    = "Выгрузить полный отчет 📋"
BUTTON_BACK           = "Назад в главное меню 🔙"