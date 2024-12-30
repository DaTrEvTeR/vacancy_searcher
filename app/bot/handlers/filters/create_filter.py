from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.bot.keyboards.filters.callback_data import FilterCBD
from app.bot.keyboards.filters.get_edit_filter_kb import get_edit_filter_kb
from app.bot.utils.base_filter_schema import FilterSchema
from app.bot.utils.get_filter_msg import get_filter_msg_from_schema
from app.config.enums import FilterAction

create_router = Router(name="create")


# noinspection PyTypeChecker
@create_router.callback_query(FilterCBD.filter(F.action == FilterAction.create))
async def create_filter(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    filt_obj = data.get("filt_obj", None)
    if filt_obj is None:
        filt_obj = FilterSchema()
        data["filt_obj"] = filt_obj
        await state.set_data(data)

    msg = get_filter_msg_from_schema(filt_obj)
    kb = get_edit_filter_kb(filt_obj)

    await cb.message.edit_text(text=msg, reply_markup=kb)
