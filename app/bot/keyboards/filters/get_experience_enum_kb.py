from app.bot.keyboards.filters.callback_data import EditExperience
from app.bot.keyboards.get_inline_kb import get_inline_kb
from app.config.enums import ExperienceEnum, enum_to_str


def get_experience_enum_kb():
    sizes = []
    btns = {}

    for member in ExperienceEnum:
        btns[enum_to_str[member]] = EditExperience(val=member).pack()
        sizes.append(1)

    return get_inline_kb(sizes, btns)
