from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    @abstractmethod
    def get_vacancies(self, filt_obj) -> List:  # todo: list[VacancyModel] when release VacancyModel
        pass
