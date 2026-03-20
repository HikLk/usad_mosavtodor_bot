# main.py
import asyncio
import logging

from create_bot import create_bot_and_dispatcher

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    bot, dp = create_bot_and_dispatcher()

    await dp.start_polling(
        bot,
        allowed_updates=["message"],
        drop_pending_updates=True
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен")