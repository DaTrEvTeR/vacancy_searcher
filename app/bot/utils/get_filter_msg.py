from app.bot.utils.base_filter_schema import FilterSchema
from app.config.enums import enum_to_str
from app.db.models import Filter


def get_filter_msg(filt_obj: Filter) -> str:
    title = filt_obj.title
    exp = enum_to_str[filt_obj.experience]
    remote = "так" if filt_obj.only_remote else "ні"
    sites_names_list = (site.site_name for site in filt_obj.sites)
    sites_list = "\n  - " + "\n  - ".join(sites_names_list)
    return f"Заголовок: {title}\n" f"Досвід роботи: {exp}\n" f"Тільки віддалено: {remote}\n" f"Сайти: {sites_list}"


def get_filter_msg_from_schema(filt_obj: FilterSchema) -> str:
    waiting = "очікується"
    title = filt_obj.title if filt_obj.title else waiting
    exp = enum_to_str[filt_obj.experience] if filt_obj.experience else waiting
    remote = "так" if filt_obj.only_remote else "ні"
    if filt_obj.sites:
        sites_names_list = (site for site in filt_obj.sites)
        sites_list = "\n  - " + "\n  - ".join(sites_names_list)
    else:
        sites_list = waiting
    return f"Заголовок: {title}\n" f"Досвід роботи: {exp}\n" f"Тільки віддалено: {remote}\n" f"Сайти: {sites_list}"
