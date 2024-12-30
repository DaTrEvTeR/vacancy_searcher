from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.keyboards.filters.callback_data import FilterCBD
from app.bot.keyboards.filters.get_edit_filter_kb import get_edit_filter_kb
from app.bot.midlewares.db import DataBaseSession
from app.bot.utils.base_filter_schema import FilterSchema
from app.bot.utils.get_filter_msg import get_filter_msg_from_schema
from app.config.enums import FilterAction
from app.db.db import session_maker
from app.db.models import Filter

update_router = Router(name="edit")
update_router.callback_query.middleware(DataBaseSession(session_maker))


# noinspection PyTypeChecker
@update_router.callback_query(FilterCBD.filter(F.action == FilterAction.update))
async def edit_router(cb: CallbackQuery, callback_data: FilterCBD, db: AsyncSession, state: FSMContext):
    old_filt = await Filter.read_one(db, id=callback_data.filter_id)
    data = await state.get_data()
    sites = [site.site_name for site in old_filt.sites]
    filt_obj = FilterSchema(
        id=old_filt.id,
        title=old_filt.title,
        experience=old_filt.experience,
        only_remote=old_filt.only_remote,
        sites=sites,
    )
    data["filt_obj"] = filt_obj
    await state.set_data(data)

    msg = get_filter_msg_from_schema(filt_obj)
    kb = get_edit_filter_kb(filt_obj)

    await cb.message.edit_text(text=msg, reply_markup=kb)
