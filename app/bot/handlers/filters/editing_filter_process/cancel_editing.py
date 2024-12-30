from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.bot.keyboards.filters.callback_data import EditFilterCBD
from app.bot.keyboards.filters.continue_kb import continue_kb
from app.bot.keyboards.filters.confirm_cancel_kb import confirm_cancel_kb
from app.config.enums import EditFilterAction

cancel_router = Router(name="cancel_router")


@cancel_router.callback_query(EditFilterCBD.filter(F.action == EditFilterAction.cancel))
async def cancel(cb: CallbackQuery):
    txt = "Ви впевнені, що хочете скасувати редагування?"
    kb = confirm_cancel_kb
    await cb.message.edit_text(text=txt, reply_markup=kb)


@cancel_router.callback_query(F.data == "edit:cancel")
async def cancel_confirm(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    del data["filt_obj"]
    await state.set_data(data)
    txt = "Зміни скасовано"
    kb = continue_kb()
    await cb.message.edit_text(text=txt, reply_markup=kb)
