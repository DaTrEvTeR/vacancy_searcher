from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.keyboards.filters.callback_data import FilterCBD, DeleteCBD
from app.bot.keyboards.filters.confirm_delete_kb import confirm_delete_kb
from app.bot.keyboards.filters.continue_kb import continue_kb
from app.bot.midlewares.db import DataBaseSession
from app.config.enums import FilterAction
from app.db.db import session_maker
from app.db.models import Filter

delete_router = Router(name="cancel_router")
delete_router.callback_query.middleware(DataBaseSession(session_maker))


@delete_router.callback_query(FilterCBD.filter(F.action == FilterAction.delete))
async def cancel(cb: CallbackQuery, callback_data: FilterCBD):
    txt = "Ви впевнені, що хочете видалити фільтр?"
    kb = confirm_delete_kb(callback_data.filter_id)
    await cb.message.edit_text(text=txt, reply_markup=kb)


@delete_router.callback_query(DeleteCBD.filter())
async def cancel_confirm(cb: CallbackQuery, callback_data: DeleteCBD, db: AsyncSession, state: FSMContext):
    filt_id = callback_data.filter_id
    statement = delete(Filter).where(Filter.id == filt_id)
    await db.execute(statement)
    await db.commit()
    data = await state.get_data()
    del data["user_filters"]
    await state.set_data(data)

    txt = "Фільтр видалено"
    kb = continue_kb()
    await cb.message.edit_text(text=txt, reply_markup=kb)
