from bs4 import BeautifulSoup

from app.config.enums import ExperienceEnum
from app.db.models import Filter
from app.vacancies_search.base.abc.parser_abc import Parser


class WorkUaParser(Parser):
    filt_obj: Filter
    str_exp_to_exp_enum_map = {
        "Без досвіду": ExperienceEnum.less_than_1_year,
        "Досвід роботи від 1 року": ExperienceEnum.one_to_three_years,
        "Досвід роботи від 2 років": ExperienceEnum.three_to_five_years,
        "Досвід роботи від 5 років": ExperienceEnum.more_than_5_years,
    }

    def parse_data(self, data: BeautifulSoup, last_sent_link: str | None = None) -> list[dict]:
        vacancies = data.select("div.card.card-hover.card-visited.wordwrap.job-link.js-job-link-blank")
        self.remove_irrelevant_vacancies(vacancies)

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

    def remove_irrelevant_vacancies(self, vacancies: list) -> None:
        vacancy_to_req_exp_map = dict()
        for v in vacancies:
            splitted_text = v.find("p").text.split(".")
            str_exp = "Без досвіду"
            if splitted_text[1].strip().startswith("Досвід роботи від "):
                str_exp = splitted_text[1].strip()
            elif splitted_text[2].strip().startswith("Досвід роботи від "):
                str_exp = splitted_text[2].strip()
            vacancy_to_req_exp_map[v] = str_exp

        to_delete = []
        for vac, exp in vacancy_to_req_exp_map.items():
            if self.str_exp_to_exp_enum_map[exp] != self.filt_obj.experience:
                to_delete.append(vac)

        for vac in to_delete:
            vacancies.remove(vac)
