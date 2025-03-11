from bs4 import BeautifulSoup

from app.db.models import Filter
from app.vacancies_search.base.base_strategy import BaseStrategy
from app.vacancies_search.concrete_parsers.work_ua_parser import WorkUaParser
from app.vacancies_search.concrete_scrapers.work_ua_scrapper import WorkUaScraper


class WorkUaStrategy(BaseStrategy):
    __site_name__ = "work.ua"

    _scraper: type[WorkUaScraper] = WorkUaScraper
    _parser: type[WorkUaParser] = WorkUaParser

    @classmethod
    async def get_vacancies(cls, filt_obj: Filter, last_sent_link: str | None = None) -> list[dict]:
        proccesing: bool = True
        page = 0
        res = []

        while proccesing:
            page += 1

            data = await cls._scraper().get_data(filt_obj=filt_obj, page=page)

            soup = BeautifulSoup(data, "lxml")
            if last_sent_link:
                links = [a["href"] for a in soup.select("h2.my-0 > a") if "href" in a.attrs]
                if last_sent_link in links:
                    proccesing = False
            if soup.select_one("ul.pagination.hidden-xs > li.disabled.add-left-default"):
                proccesing = False

            parser = cls._parser()
            parser.filt_obj = filt_obj

            res += parser.parse_data(soup, last_sent_link)

        return res
