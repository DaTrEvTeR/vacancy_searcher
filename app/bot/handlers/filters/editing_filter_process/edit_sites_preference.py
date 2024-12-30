from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.keyboards.filters.callback_data import EditFilterCBD, FilterCBD, SitesCBD
from app.bot.utils.base_filter_schema import FilterSchema
from app.config.enums import EditFilterAction, FilterAction

edit_sites_preference_router = Router(name="edit_sites_preference")


emoji_map = {
    True: "✅",
    False: "❌",
}


# todo: redo it when create the model parsers
@edit_sites_preference_router.callback_query(EditFilterCBD.filter(F.action == EditFilterAction.sites))
async def edit_sites(cb: CallbackQuery, state: FSMContext):
    ### for test
    sites = ["work.ua", "robota.ua", "dou.ua", "djinny.com"]
    ###
    data = await state.get_data()
    filt_obj: FilterSchema = data.get("filt_obj")
    msg = ""
    kb = InlineKeyboardBuilder()
    kb.max_width = 1
    for site in sites:
        emoji = emoji_map[site in filt_obj.sites]
        msg += f"{emoji}  {site}\n"
        kb.add(InlineKeyboardButton(text=site, callback_data=SitesCBD(site_name=site).pack()))
    kb.add(InlineKeyboardButton(text="Назад", callback_data=FilterCBD(action=FilterAction.create).pack()))
    kb = kb.as_markup()

    await cb.message.edit_text(text=msg, reply_markup=kb)


@edit_sites_preference_router.callback_query(SitesCBD.filter())
async def set_preference(cb: CallbackQuery, callback_data: SitesCBD, state: FSMContext):
    ### for test
    sites = ["work.ua", "robota.ua", "dou.ua", "djinny.com"]
    ###
    data = await state.get_data()
    filt_obj: FilterSchema = data.get("filt_obj")
    site = callback_data.site_name
    if site in filt_obj.sites:
        filt_obj.sites.remove(site)
    else:
        filt_obj.sites.append(site)

    msg = ""
    kb = InlineKeyboardBuilder()
    kb.max_width = 1
    for site in sites:
        emoji = emoji_map[site in filt_obj.sites]
        msg += f"{emoji}  {site}\n"
        kb.add(InlineKeyboardButton(text=site, callback_data=SitesCBD(site_name=site).pack()))
    kb.add(InlineKeyboardButton(text="Назад", callback_data=FilterCBD(action=FilterAction.create).pack()))
    kb = kb.as_markup()

    await cb.message.edit_text(text=msg, reply_markup=kb)
