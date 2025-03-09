from typing import List
from bs4 import BeautifulSoup

from app.db.models import Filter
from app.vacancies_search.base.base_strategy import BaseStrategy
from app.vacancies_search.concrete_parsers.work_ua_parser import WorkUaParser
from app.vacancies_search.concrete_scrapers.work_ua_scrapper import WorkUaScraper


class WorkUaStrategy(BaseStrategy):
    __site_name__ = "work.ua"

    _scraper: WorkUaScraper = WorkUaScraper()
    _parser: WorkUaParser = WorkUaParser()

    @classmethod
    async def get_vacancies(cls, filt_obj: Filter) -> List:  # todo: list[VacancyModel] when release VacancyModel
        proccesing: bool = True
        page = 1
        res = []

        while proccesing:
            data = await cls._scraper.get_data(filt_obj=filt_obj, page=page)

            soup = BeautifulSoup(data, "lxml")
            soup.find()  ### todo: rework when release last link storage
            if not soup.select_one("#pjax-job-list > nav > ul.pagination.hidden-xs > li.no-style.add-left-default"):
                proccesing = False
            else:
                page += 1

            res += cls._parser.parse_data(soup)

        return res
