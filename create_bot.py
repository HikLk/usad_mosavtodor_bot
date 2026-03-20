# create_bot.py
from aiogram import Bot, Dispatcher

from config import TOKEN

# Импорт роутеров из handlers
from handlers.common import router as common_router
from handlers.winter import router as winter_router
from handlers.summer import router as summer_router
from handlers.contractors import router as contractors_router

# Если у вас есть другие роутеры — добавляйте их сюда аналогично


def create_bot_and_dispatcher() -> tuple[Bot, Dispatcher]:
    """
    Создаёт экземпляры Bot и Dispatcher и подключает все роутеры.
    Возвращает кортеж (bot, dp)
    """
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Подключаем роутеры
    # Порядок важен: более общие/командные роутеры обычно ниже
    dp.include_router(common_router)       # /start, назад, меню летних работ
    dp.include_router(winter_router)       # зимние отчёты
    dp.include_router(summer_router)       # летние отчёты
    dp.include_router(contractors_router)  # подрядчики

    # Если позже добавите ещё роутеры — подключайте здесь
    # dp.include_router(другой_router)

    return bot, dp