from aiogram import Router

from app.bot.handlers.filters.editing_filter_process.cancel_editing import cancel_router
from app.bot.handlers.filters.editing_filter_process.edit_experience import edit_expirience_router
from app.bot.handlers.filters.editing_filter_process.edit_remote import edit_remote_router
from app.bot.handlers.filters.editing_filter_process.edit_sites_preference import edit_sites_preference_router
from app.bot.handlers.filters.editing_filter_process.edit_tiitle import edit_title_router
from app.bot.handlers.filters.editing_filter_process.save_filter import save_router

editing_router = Router(name="editing")

editing_router.include_routers(
    edit_title_router,
    edit_expirience_router,
    edit_remote_router,
    edit_sites_preference_router,
    save_router,
    cancel_router,
)
