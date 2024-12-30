from aiogram import Router

from app.bot.handlers.filters.create_filter import create_router
from app.bot.handlers.filters.de_activate_filter import de_activate_router
from app.bot.handlers.filters.delete_filter import delete_router
from app.bot.handlers.filters.edit_filter import update_router
from app.bot.handlers.filters.editing_filter_process import editing_router
from app.bot.handlers.filters.read_filter import read_router


filters_router = Router(name="filters")

filters_router.include_routers(
    read_router,
    create_router,
    editing_router,
    delete_router,
    update_router,
    de_activate_router,
)
