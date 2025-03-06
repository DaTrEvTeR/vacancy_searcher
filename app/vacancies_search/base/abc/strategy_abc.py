from abc import ABC, abstractmethod
from typing import List

from app.db.models import Filter
from app.vacancies_search.base.abc.parser_abc import Parser
from app.vacancies_search.base.abc.scraper_abc import Scraper


class Strategy(ABC):
    __site_name__: str

    _scraper: Scraper
    _parser: Parser

    @abstractmethod
    async def get_vacancies(self, filt_obj: Filter) -> List:  # todo: list[VacancyModel] when release VacancyModel
        pass
