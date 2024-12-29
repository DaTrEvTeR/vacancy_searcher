from .config import bot, dp
from .handlers.main_menu import main_menu
from .handlers.filters import filters_router

dp.include_routers(
    main_menu,
    filters_router,
)
