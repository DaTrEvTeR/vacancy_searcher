from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.bot.keyboards.filters.callback_data import EditFilterCBD
from app.bot.keyboards.filters.get_edit_filter_kb import get_edit_filter_kb
from app.bot.utils.base_filter_schema import FilterSchema
from app.bot.utils.get_filter_msg import get_filter_msg_from_schema
from app.config.enums import EditFilterAction

edit_remote_router = Router(name="edit_remote")


@edit_remote_router.callback_query(EditFilterCBD.filter(F.action == EditFilterAction.remote))
async def edit_remote(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    filt_obj: FilterSchema = data.get("filt_obj")
    filt_obj.only_remote = not filt_obj.only_remote
    data["filt_obj"] = filt_obj
    await state.set_data(data)
    txt = get_filter_msg_from_schema(filt_obj)
    kb = get_edit_filter_kb(filt_obj)
    await cb.message.edit_text(text=txt, reply_markup=kb)
