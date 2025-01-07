from typing import List

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

    def get_vacancies(self, filt_obj=None) -> List:  # todo: list[VacancyModel] when release VacancyModel
        return self._strategy.get_vacancies(filt_obj=filt_obj)
