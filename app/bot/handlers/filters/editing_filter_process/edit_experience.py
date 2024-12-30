from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.bot.keyboards.filters.callback_data import EditFilterCBD, EditExperience
from app.bot.keyboards.filters.get_experience_enum_kb import get_experience_enum_kb
from app.bot.keyboards.filters.get_edit_filter_kb import get_edit_filter_kb
from app.bot.utils.base_filter_schema import FilterSchema
from app.bot.utils.get_filter_msg import get_filter_msg_from_schema
from app.config.enums import EditFilterAction

edit_expirience_router = Router(name="edit_expirience")


@edit_expirience_router.callback_query(EditFilterCBD.filter(F.action == EditFilterAction.exp))
async def edit_exp(cb: CallbackQuery):
    txt = "Виберіть досвід у спеціалізації"
    kb = get_experience_enum_kb()
    print(kb)
    await cb.message.edit_text(text=txt, reply_markup=kb)


@edit_expirience_router.callback_query(EditExperience.filter())
async def input_exp(cb: CallbackQuery, callback_data: EditExperience, state: FSMContext):
    data = await state.get_data()
    filt_obj: FilterSchema = data.get("filt_obj")
    filt_obj.experience = callback_data.val
    data["filt_obj"] = filt_obj
    await state.set_data(data)
    txt = get_filter_msg_from_schema(filt_obj)
    kb = get_edit_filter_kb(filt_obj)
    await cb.message.edit_text(text=txt, reply_markup=kb)
