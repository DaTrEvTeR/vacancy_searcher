from typing import Optional
from uuid import UUID

from aiogram.filters.callback_data import CallbackData

from app.config.enums import EditFilterAction, ExperienceEnum, FilterAction


class EditFilterCBD(CallbackData, prefix="edit_filter"):  # type: ignore
    action: EditFilterAction


class EditExperience(CallbackData, prefix="inpexp"):  # type: ignore
    val: ExperienceEnum


class FilterCBD(CallbackData, prefix="filter"):  # type: ignore
    action: FilterAction
    filter_id: Optional[UUID] = None


class DeleteCBD(CallbackData, prefix="delete"):  # type: ignore
    filter_id: UUID


class SitesCBD(CallbackData, prefix="sites"):  # type: ignore
    site_name: str
