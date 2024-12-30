from typing import Optional
from uuid import UUID

from app.bot.keyboards.filters.callback_data import FilterCBD
from app.bot.keyboards.get_inline_kb import get_inline_kb
from app.config.enums import FilterAction
from app.config.settings import settings
from app.db.models import Filter


def get_read_filter_kb(user_filters: list[UUID], filt_obj: Optional[Filter] = None):
    size = []
    btns = {}

    # action with filter buttons
    if filt_obj:
        # syb/unsub button
        if filt_obj.active:
            btns["Деактивувати"] = FilterCBD(action=FilterAction.de_activate, filter_id=filt_obj.id).pack()
        else:
            btns["Активувати"] = FilterCBD(action=FilterAction.de_activate, filter_id=filt_obj.id).pack()
        size.append(1)

        # delete button
        btns["Видалити"] = FilterCBD(action=FilterAction.delete, filter_id=filt_obj.id).pack()

        # update button
        btns["Змінити"] = FilterCBD(action=FilterAction.update, filter_id=filt_obj.id).pack()
        size.append(2)

        # nav buttons
        filt_index = user_filters.index(filt_obj.id)
        nav_btns_count = 0
        # prev button
        if filt_index != 0:
            btns["Минулий"] = FilterCBD(action=FilterAction.read, filter_id=user_filters[filt_index - 1]).pack()
            nav_btns_count += 1
        # next button
        if filt_index != len(user_filters) - 1:
            btns["Наcтупний"] = FilterCBD(action=FilterAction.read, filter_id=user_filters[filt_index + 1]).pack()
            nav_btns_count += 1
        if nav_btns_count:
            size.append(nav_btns_count)

    # new filter button
    if len(user_filters) < settings.max_filters_for_one_user:
        btns["Сторити новий"] = FilterCBD(action=FilterAction.create).pack()
        size.append(1)

    return get_inline_kb(size, btns)
