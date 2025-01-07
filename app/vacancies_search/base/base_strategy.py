from typing import List

from app.vacancies_search.base.abc.parser_abc import Parser
from app.vacancies_search.base.abc.scraper_abc import Scraper
from app.vacancies_search.base.abc.strategy_abc import Strategy
from app.vacancies_search.base.strategy_registry import StrategyRegistry


class BaseStrategy(Strategy):
    __site_name__: str

    def __init__(self, scraper: Scraper, parser: Parser):
        self.scraper = scraper
        self.parser = parser

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        StrategyRegistry.register(cls)

    def get_vacancies(self, filt_obj) -> List:  # todo: list[VacancyModel] when release VacancyModel
        data = self.scraper.get_data(filt_obj)
        return self.parser.parse_data(data)
