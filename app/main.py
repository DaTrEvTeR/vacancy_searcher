import logging

from app.bot import bot, dp
from app.utils.logging import init_logging
from app.utils.init_strategies import init_sites_in_db


async def main():
    init_logging()
    await init_sites_in_db()
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logging.critical(f"{e}\n\napp shuts down")
