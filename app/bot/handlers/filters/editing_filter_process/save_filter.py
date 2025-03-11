import logging
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.keyboards.filters.callback_data import EditFilterCBD
from app.bot.keyboards.filters.continue_kb import continue_kb
from app.bot.midlewares.db import DataBaseSession
from app.bot.utils.base_filter_schema import FilterSchema
from app.config.enums import EditFilterAction
from app.db.db import session_maker
from app.db.models import Filter, Site

save_router = Router(name="save")
save_router.callback_query.middleware(DataBaseSession(session_maker))


@save_router.callback_query(EditFilterCBD.filter(F.action == EditFilterAction.save))
async def save(cb: CallbackQuery, db: AsyncSession, state: FSMContext):
    data = await state.get_data()
    filt_schema: FilterSchema = data.get("filt_obj")
    if not filt_schema.title:
        return await cb.answer("Вкажіть спеціальність")
    if not filt_schema.experience:
        return await cb.answer("Вкажіть досвід")
    if not filt_schema.sites:
        return await cb.answer("Вкажіть сайти")
    statement = select(Site).where(Site.site_name.in_(filt_schema.sites))
    sites = (await db.execute(statement)).scalars().fetchall()
    filt_id = filt_schema.id
    if filt_id:
        filt_obj = await Filter.read_one(db, id=filt_id)
        filt_obj.title = filt_schema.title
        filt_obj.experience = filt_schema.experience
        filt_obj.only_remote = filt_schema.only_remote
        filt_obj.user_id = cb.from_user.id
        filt_obj.sites = sites
    else:
        filt_obj = Filter(
            title=filt_schema.title,
            experience=filt_schema.experience,
            only_remote=filt_schema.only_remote,
            user_id=cb.from_user.id,
            sites=sites,
        )
    if filt_obj.id:
        await filt_obj.update(db)
    else:
        await filt_obj.create(db)
    del data["filt_obj"]
    try:
        del data["user_filters"]
    except KeyError:
        logging.warning("Attempted to delete the custom filter cache, but the cache was not initialized.")
    await state.set_data(data)
    txt = "Фільтр збережено"
    kb = continue_kb(filt_id)
    await cb.message.edit_text(text=txt, reply_markup=kb)
