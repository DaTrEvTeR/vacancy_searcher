from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.keyboards.main_menu import get_main_menu_kb
from app.bot.midlewares.db import DataBaseSession
from app.db.db import session_maker
from app.db.models import User

main_menu = Router(name="main_menu")
main_menu.message.middleware(DataBaseSession(session_maker))


@main_menu.message(CommandStart())
async def start(msg: Message, db: AsyncSession):
    user = await User.read_one(db, id=msg.from_user.id)
    if not user:
        await User(id=msg.from_user.id).create(db)

    await msg.answer("Головное меню", reply_markup=get_main_menu_kb())


@main_menu.message(Command("menu"))
async def menu(msg: Message):
    await msg.answer("Головное меню", reply_markup=get_main_menu_kb())


@main_menu.callback_query(F.data == "help")
async def help(cb: CallbackQuery):
    await cb.message.edit_text(
        "Цей бот використовує багаторівневе `Inline` меню, "
        "тому для його використання не потрібно читати опис команд або прописувати спеціальні слова."
        "\n\nЩоб знову викликати головне меню - використайте команду /menu"
        "\n\nДля зміни мови інтерфейсу з української на англійську використайте команду /chl",
        reply_markup=get_main_menu_kb(),
    )


@main_menu.callback_query(F.data == "about")
async def about(cb: CallbackQuery):
    await cb.message.edit_text(
        "Цей бот розробив @datrevter"
        "\nЯкщо у вас є зауваження або пропозиція по роботі бота - буду радий поспілкуватися"
        "\n\nГоловна ціль цього проекту облегшити пошук вакансій на великій кількості платформ. "
        "Бот замість вас 'обходить' усі вказані платформи роботодавців за вказаними фільтрами, "
        "що домогає вам зосередитися на покращенні своїх навичок"
        "\n\nЯкщо мені вдалося допомогти вам - буду вдячний за зворотний зв'язок",
        reply_markup=get_main_menu_kb(),
    )
