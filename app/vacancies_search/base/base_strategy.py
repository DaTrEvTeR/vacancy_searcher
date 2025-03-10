from app.db.models import Filter
from app.vacancies_search.base.abc.strategy_abc import Strategy
from app.vacancies_search.base.strategy_registry import StrategyRegistry


class BaseStrategy(Strategy):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        StrategyRegistry.register(cls)

    async def get_vacancies(self, filt_obj: Filter, last_sent_link: str) -> list[dict]:
        data = self._scraper.get_data(filt_obj)
        return self._parser.parse_data(data, last_sent_link)
