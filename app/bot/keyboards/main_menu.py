from app.bot.keyboards.filters.callback_data import FilterCBD
from app.bot.keyboards.get_inline_kb import get_inline_kb
from app.config.enums import FilterAction


def get_main_menu_kb():
    sizes = [1, 2]
    buttons = {
        "Фільтри": FilterCBD(action=FilterAction.read).pack(),
        "Про проект": "about",
        "Довідка": "help",
    }
    return get_inline_kb(
        sizes=sizes,
        buttons=buttons,
    )
