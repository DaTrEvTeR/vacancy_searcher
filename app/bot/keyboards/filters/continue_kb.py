from typing import Optional
from uuid import UUID

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.keyboards.filters.callback_data import FilterCBD
from app.config.enums import FilterAction


def continue_kb(filt_id: Optional[UUID] = None):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Продовжити", callback_data=FilterCBD(action=FilterAction.read, filter_id=filt_id).pack()
                )
            ]
        ]
    )
