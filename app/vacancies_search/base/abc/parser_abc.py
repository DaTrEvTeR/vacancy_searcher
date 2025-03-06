from abc import ABC, abstractmethod
from typing import List
from bs4 import BeautifulSoup


class Parser(ABC):
    @abstractmethod
    def parse_data(self, data: BeautifulSoup) -> List:  # todo: list[VacancyModel] when release VacancyModel
        pass
