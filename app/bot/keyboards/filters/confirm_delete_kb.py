from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.keyboards.filters.callback_data import FilterCBD, DeleteCBD
from app.config.enums import FilterAction


def confirm_delete_kb(filter_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Так", callback_data=DeleteCBD(filter_id=filter_id).pack())],
            [
                InlineKeyboardButton(
                    text="Ні", callback_data=FilterCBD(action=FilterAction.read, filter_id=filter_id).pack()
                )
            ],
        ]
    )
