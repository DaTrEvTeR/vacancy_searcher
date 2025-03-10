from bs4 import BeautifulSoup

from app.vacancies_search.base.abc.parser_abc import Parser


class WorkUaParser(Parser):
    def parse_data(self, data: BeautifulSoup, last_sent_link: str | None = None) -> list[dict]:
        vacancies = data.select(
            "#pjax-jobs-list > div.card.card-hover.card-visited.wordwrap.job-link.js-job-link-blank"
        )
        res = []
        for vacancy in vacancies:
            title_tag = vacancy.find("a")

            if last_sent_link:
                if title_tag["href"] == last_sent_link:
                    break

            res.append(
                {
                    "title": title_tag.text,
                    "href": "https://www.work.ua" + title_tag["href"],
                }
            )

        return res
