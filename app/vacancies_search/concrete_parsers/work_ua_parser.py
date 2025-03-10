from bs4 import BeautifulSoup

from app.vacancies_search.base.abc.parser_abc import Parser


class WorkUaParser(Parser):
    def parse_data(self, data: BeautifulSoup) -> list[dict]:
        vacancies = data.select(
            "#pjax-jobs-list > div.card.card-hover.card-visited.wordwrap.job-link.js-job-link-blank"
        )
        res = []
        for vacancy in vacancies:
            if vacancy.find("a")["href"] == "/":  # todo: rework when release last_link
                break
            title = vacancy.find("a")
            res.append(
                {
                    "title": title.text,
                    "href": "https://www.work.ua" + title["href"],
                }
            )
        return res
