from app.bot.keyboards.filters import FiltersCBData
from app.bot.keyboards.get_inline_kb import get_inline_kb


def get_main_menu_kb():
    sizes = [2, 1]
    buttons = {
        "Фільтри": FiltersCBData(menu_name="list", action="show"),
        "Про проект": "about",
        "Довідка": "help",
    }
    return get_inline_kb(
        sizes=sizes,
        buttons=buttons,
    )
