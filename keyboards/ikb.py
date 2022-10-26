from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import RZN_TYPES

ikb_type = InlineKeyboardMarkup(row_width=1)
for btn in RZN_TYPES:
    ikb_type.add(InlineKeyboardButton(text=btn[1], callback_data='type_' + str(btn[0])))

btn_cansel = InlineKeyboardButton(text='Отмена', callback_data='btn_cansel')
ikb_type.add(btn_cansel)

ikb_cansel = InlineKeyboardMarkup(row_width=1)
ikb_cansel.add(btn_cansel)


def generate_ikb_list_tasks(tasks):
    ikb_tasks = InlineKeyboardMarkup(row_width=1)
    for task in tasks:
        ikb_tasks.add(InlineKeyboardButton(text=task['title'], url=task['url']))
    return ikb_tasks


