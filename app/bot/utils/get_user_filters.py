from typing import Optional
from uuid import UUID

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Filter


async def get_user_filters(
    cb: CallbackQuery, db: AsyncSession, state: FSMContext, data: Optional[dict] = None
) -> list[UUID]:
    if data is None:
        data = await state.get_data()
    user_filters = data.get("user_filters", None)
    if user_filters is None:
        user_filters = await Filter.get_user_filters_ids(db, cb.from_user.id)
        data["user_filters"] = user_filters
        await state.set_data(data)
    return user_filters
