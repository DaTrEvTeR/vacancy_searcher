from aiogram import Router, F
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

de_activate_router = Router(name="de_activate")
de_activate_router.callback_query.middleware(DataBaseSession(session_maker))


@de_activate_router.callback_query(FilterCBD.filter(F.action == FilterAction.de_activate))
async def de_activate(cb: CallbackQuery, callback_data: FilterCBD, db: AsyncSession, state: FSMContext):
    data = await state.get_data()
    filt_obj = await Filter.read_one(db, id=callback_data.filter_id)
    filt_obj.active = not filt_obj.active
    db.add(filt_obj)
    await db.commit()

    user_filters = await get_user_filters(cb, db, state, data)
    msg = get_filter_msg(filt_obj)
    kb = get_read_filter_kb(user_filters, filt_obj)
    await cb.message.edit_text(text=msg, reply_markup=kb)
