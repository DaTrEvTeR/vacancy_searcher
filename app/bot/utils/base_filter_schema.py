from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.config.enums import ExperienceEnum


class FilterSchema(BaseModel):
    id: Optional[UUID] = None
    title: str = ""
    experience: Optional[ExperienceEnum] = None
    only_remote: bool = False
    sites: list[str] = list()
