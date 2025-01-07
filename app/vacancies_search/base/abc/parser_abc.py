from abc import ABC, abstractmethod
from typing import List


class Parser(ABC):
    @abstractmethod
    def parse_data(self, data) -> List:  # todo: list[VacancyModel] when release VacancyModel
        pass
