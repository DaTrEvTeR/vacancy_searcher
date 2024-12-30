from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import CallbackQuery, Message

from app.bot.keyboards.filters.callback_data import EditFilterCBD
from app.bot.keyboards.filters.get_edit_filter_kb import get_edit_filter_kb
from app.bot.utils.base_filter_schema import FilterSchema
from app.bot.utils.get_filter_msg import get_filter_msg_from_schema
from app.config.enums import EditFilterAction

edit_title_router = Router(name="edit_title")
waiting_title_input = State()


@edit_title_router.callback_query(EditFilterCBD.filter(F.action == EditFilterAction.title))
async def edit_title(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    data["editing_msg"] = cb.message
    await state.set_data(data)
    await state.set_state(waiting_title_input)
    await cb.message.edit_text(
        text="Введіть назву спеціальності\n"
        "<blockquote>Рекомендується вводити узагальнену назву, "
        "оскільки, наприклад, пошук `python` знайде умовно "
        "40 вакансій, а `python developer` 22</blockquote>\n"
    )


@edit_title_router.message(waiting_title_input)
async def input_title(msg: Message, state: FSMContext):
    data = await state.get_data()
    filt_obj: FilterSchema = data.get("filt_obj")
    new_title = msg.text.strip()
    filt_obj.title = new_title
    data["filt_obj"] = filt_obj
    await state.set_data(data)
    await state.set_state(None)

    txt = get_filter_msg_from_schema(filt_obj)
    kb = get_edit_filter_kb(filt_obj)

    await msg.delete()
    editing_msg: Message = data.get("editing_msg")
    await editing_msg.edit_text(text=txt, reply_markup=kb)
