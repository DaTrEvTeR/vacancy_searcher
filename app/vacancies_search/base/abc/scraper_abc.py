from abc import ABC, abstractmethod
from typing import Union


class Scraper(ABC):
    @abstractmethod
    def get_data(self, filt_obj) -> Union[str, dict]:
        pass
