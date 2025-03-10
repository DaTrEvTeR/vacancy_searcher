from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class Parser(ABC):
    @abstractmethod
    def parse_data(self, data: BeautifulSoup, last_sent_link: str) -> list[dict]:
        pass
