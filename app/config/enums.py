from enum import Enum


class ExperienceEnum(Enum):
    less_than_1_year = "0"
    one_to_three_years = "1"
    three_to_five_years = "2"
    more_than_5_years = "3"


enum_to_str = {
    ExperienceEnum.less_than_1_year: "меньше одного року",
    ExperienceEnum.one_to_three_years: "від 1 до 3 років",
    ExperienceEnum.three_to_five_years: "від 3 до 5 років",
    ExperienceEnum.more_than_5_years: "більше 5 років",
}


class FilterAction(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
    de_activate = "de_activate"


class EditFilterAction(Enum):
    title = "title"
    exp = "exp"
    remote = "remote"
    sites = "sites"
    save = "save"
    cancel = "cancel"
