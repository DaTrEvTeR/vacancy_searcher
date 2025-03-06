from typing import List
from bs4 import BeautifulSoup

from app.vacancies_search.base.abc.parser_abc import Parser


class WorkUaParser(Parser):
    def parse_data(self, data: BeautifulSoup) -> List:  # todo: list[VacancyModel] when release VacancyModel
        vacancies = data.select(
            "#pjax-jobs-list > div.card.card-hover.card-visited.wordwrap.job-link.js-job-link-blank"
        )
        res = []
        for vacancy in vacancies:
            if vacancy.find("a")["href"] == "/":  # todo: rework when release last_link
                break
            title = vacancy.find("a")
            salary = vacancy.select_one("div:nth-child(2) > span.strong-600")
            online = vacancy.find("div", class_="mt-xs").find("span", text=", Дистанційно")
            res.append(
                {
                    "title": title.text,
                    "href": "https://www.work.ua" + title["href"],
                    "salary": salary.text if salary else None,
                    "online": True if online else False,
                }
            )
        return res
