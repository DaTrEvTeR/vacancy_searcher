import logging

from app.bot.config import bot, dp
from app.utils.logging import init_logging


async def main():
    init_logging()
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logging.critical(f"{e}\n\napp shuts down")
