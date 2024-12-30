from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.keyboards.filters.callback_data import FilterCBD
from app.config.enums import FilterAction

confirm_cancel_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Так", callback_data="edit:cancel")],
        [InlineKeyboardButton(text="Ні", callback_data=FilterCBD(action=FilterAction.create).pack())],
    ]
)
