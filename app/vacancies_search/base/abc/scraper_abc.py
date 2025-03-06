from abc import ABC, abstractmethod

from app.db.models import Filter


class Scraper(ABC):
    @abstractmethod
    async def get_data(self, filt_obj: Filter, page: int = 1) -> str | dict:
        pass
