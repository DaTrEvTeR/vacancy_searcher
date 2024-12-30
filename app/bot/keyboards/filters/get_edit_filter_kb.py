from app.bot.keyboards.filters.callback_data import EditFilterCBD
from app.bot.keyboards.get_inline_kb import get_inline_kb
from app.bot.utils.base_filter_schema import FilterSchema
from app.config.enums import EditFilterAction


def get_edit_filter_kb(filt_obj: FilterSchema):
    sizes = [1] * 6
    btns = {
        "Заголовок": EditFilterCBD(action=EditFilterAction.title).pack(),
        "Досвід": EditFilterCBD(action=EditFilterAction.exp).pack(),
        "Тільки віддалено": EditFilterCBD(action=EditFilterAction.remote).pack(),
        "Сайти": EditFilterCBD(action=EditFilterAction.sites).pack(),
        "Зберігти": EditFilterCBD(action=EditFilterAction.save).pack(),
        "Скасувати": EditFilterCBD(action=EditFilterAction.cancel).pack(),
    }

    return get_inline_kb(sizes, btns)
