from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.keyboards.filters.callback_data import FilterCBD
from app.bot.keyboards.filters.get_read_filter_kb import get_read_filter_kb
from app.bot.midlewares.db import DataBaseSession
from app.bot.utils.get_filter_msg import get_filter_msg
from app.bot.utils.get_user_filters import get_user_filters
from app.config.enums import FilterAction
from app.db.db import session_maker
from app.db.models import Filter

read_router = Router(name="read")
read_router.callback_query.middleware(DataBaseSession(session_maker))


# noinspection PyTypeChecker
@read_router.callback_query(FilterCBD.filter(F.action == FilterAction.read))
async def read_filter(cb: CallbackQuery, callback_data: FilterCBD, db: AsyncSession, state: FSMContext):
    user_filters = await get_user_filters(cb, db, state)
    if (not callback_data.filter_id) and user_filters:
        callback_data.filter_id = user_filters[0]

    filt_obj: Filter | None = None
    if callback_data.filter_id:
        filt_obj = await Filter.read_one(db, id=callback_data.filter_id)

    if filt_obj:
        msg = get_filter_msg(filt_obj)
        kb = get_read_filter_kb(user_filters, filt_obj)
    else:
        msg = "У вас поки немає жодного фільтра"
        kb = get_read_filter_kb(user_filters)

    await cb.message.edit_text(text=msg, reply_markup=kb)
