from typing import List

from app.db.models import Filter
from app.vacancies_search.base.abc.strategy_abc import Strategy


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    async def get_vacancies(self, filt_obj: Filter, last_sent_link: str) -> List[dict]:
        return await self._strategy.get_vacancies(filt_obj=filt_obj, last_sent_link=last_sent_link)
