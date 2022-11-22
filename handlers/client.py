import json

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL
from shortcut import get_type_title
from bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.ikb import ikb_type, ikb_cansel, generate_ikb_list_tasks, generate_ikb_list_tasks_delete, ikb_yes_no, \
    ikb_settings
# from rzn.functions.actions import get_type_title, add_task
# from users.models import CustomUser
import asyncio
import aiohttp


class FSMClientAddTask(StatesGroup):
    type = State()
    user_id = State()
    message_id = State()
    name_md = State()
    number = State()
    date = State()


class FSMClientDelTask(StatesGroup):
    user_id = State()
    message_id = State()
    task_id = State()
    task_title = State()
    confirm = State()


async def get_user(tg_chat_id):
    params = {'tg_chat_id': tg_chat_id}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{URL}/tg/users/" + str(tg_chat_id) + "/") as resp:
            # print(resp.status)
            return await resp.text()


async def create_user(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://{URL}/tg/create_user/", data=data) as resp:
            # print(resp.status)
            print(await resp.text())


async def create_task(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://{URL}/tg/create_task/", data=data) as resp:
            # print(resp.status)
            answer = await resp.text()
            # print(answer)
            return answer


def get_msg_create_task(type_id, name_md='???', number='???', date='???') -> str:
    type_id = int(type_id)
    type_title = get_type_title(type_id)
    type_number_title = 'Вх. номер'
    if type_id == 6:
        type_number_title = 'Исх. номер'
    caption_message = ''
    if name_md == '???':
        caption_message = f"📝 <b>Введите наименование МИ</b>\n\n"
    elif number == '???':
        caption_message = f"📝 <b>Введите {type_number_title.lower()}</b>\n\n"
    elif date == '???':
        caption_message = f"📝 <b>Введите дату в формате дд.мм.гггг</b>\n\n"
    else:
        caption_message = f"✅ <b>Задача добавлена</b>\n\n"
    template_message = f"{caption_message}" \
                       f"Тип: {type_title}\n" \
                       f"Наименование МИ: {name_md}\n" \
                       f"{type_number_title}: {number}\n" \
                       f"Дата: {date}"
    return template_message


def get_msg_delete_task(type_id, type_title, title, number, date) -> str:
    type_number_title = 'Вх. номер'
    if type_id == 6:
        type_number_title = 'Исх. номер'
    caption_message = f"❌ <b>Задача удалена</b>\n\n"
    template_message = f"{caption_message}" \
                       f"Тип: {type_title}\n" \
                       f"Наименование МИ: {title}\n" \
                       f"{type_number_title}: {number}\n" \
                       f"Дата: {date}"
    return template_message


start_message = f"Добро пожаловать!\n" \
                f"Для взаимодействия с ботом используйте команды.\n" \
                f"Бот не работает в групповых чатах.\n" \
                f"За новостями и о статусе работы бота можно следить на канале [regassistant](https://t.me/regassistant). " \
                f"Также на канале можно оставить комментарий, если есть проблема/пожелание\n"


async def start(message: types.Message):
    user = {
        "tg_chat_id": message.from_user.id
    }
    if message.from_user.username is not None:
        user['tg_username'] = message.from_user.username
    if message.from_user.first_name is not None:
        user['tg_first_name'] = message.from_user.first_name
    if message.from_user.last_name is not None:
        user['tg_last_name'] = message.from_user.last_name

    res = await get_user(user["tg_chat_id"])
    if res:
        await create_user(user)
    else:
        print(res)
    await message.answer(text=start_message, parse_mode='Markdown')
    await message.delete()


async def add_task(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Выберите тип задачи', parse_mode="HTML",
                           reply_markup=ikb_type)
    await message.delete()
    await FSMClientAddTask.type.set()


async def callback_type(callback: types.CallbackQuery, state: FSMContext):
    type_id = callback.data[callback.data.find('_') + 1:]
    async with state.proxy() as data:
        data['message_id'] = callback.message.message_id
        data['tg_chat_id'] = callback.from_user.id
        data['type'] = type_id
    await callback.answer()
    await callback.message.edit_text(text=get_msg_create_task(type_id=type_id),
                                     reply_markup=ikb_cansel,
                                     parse_mode='HTML')
    await FSMClientAddTask.next()
    await FSMClientAddTask.next()
    await FSMClientAddTask.next()


async def callback_cansel(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback.message.delete()


async def add_name_md(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_md'] = message.text
        await bot.edit_message_text(message_id=data['message_id'],
                                    chat_id=message.from_user.id,
                                    text=get_msg_create_task(type_id=data['type'],
                                                             name_md=data['name_md']),
                                    reply_markup=ikb_cansel,
                                    parse_mode='HTML')
    await FSMClientAddTask.next()
    await message.delete()


async def add_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        await bot.edit_message_text(message_id=data['message_id'],
                                    chat_id=message.from_user.id,
                                    text=get_msg_create_task(type_id=data['type'],
                                                             name_md=data['name_md'],
                                                             number=data['number']),
                                    reply_markup=ikb_cansel,
                                    parse_mode='HTML')
    await FSMClientAddTask.next()
    await message.delete()


async def add_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
        await bot.edit_message_text(message_id=data['message_id'],
                                    chat_id=message.from_user.id,
                                    text=get_msg_create_task(type_id=data['type'],
                                                             name_md=data['name_md'],
                                                             number=data['number'],
                                                             date=data['date']),
                                    parse_mode='HTML')
    await FSMClientAddTask.next()
    # print(data.as_dict())
    await message.delete()
    await create_task(data.as_dict())
    # print(answer)
    await state.finish()


async def updates(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{URL}/tg/update_tasks/") as resp:
            answer = await resp.text()
        async with session.get(f"http://{URL}/tg/tg_send_updates/") as resp:
            answer = await resp.text()
            msgs = json.loads(answer)
            for msg in msgs:
                chat_id = msg['chat_id']
                taskdata_id = msg['taskdata_id']
                print(taskdata_id)
                title = msg['title']
                task_type = msg['type']
                notice = msg['notice']
                completed = msg['completed']
                url = msg['url']
                if completed:
                    msg_text = f"<strong>{title} ({task_type})</strong>\n" \
                               f"<i>{notice}</i>\n" \
                               f"<i>Задача завершена.</i>\n" \
                               f"<i>Задача удалена из списка.</i>\n" \
                               f"<a href=\"{url}\">Посмотреть на сайте РЗН</a>"
                    await bot.send_message(chat_id=chat_id, text=msg_text, parse_mode="HTML")
                else:
                    msg_text = f"<strong>{title} ({task_type})</strong>\n" \
                               f"<i>{notice}</i>\n" \
                               f"<a href=\"{url}\">Посмотреть на сайте РЗН</a>"
                    await bot.send_message(chat_id=chat_id, text=msg_text, parse_mode="HTML")
                async with session.get(f"http://{URL}/tg/tg_change_notice_1/{taskdata_id}/") as resp:
                    answer = await resp.text()


async def list_tasks(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{URL}/tg/list_tasks/{message.from_user.id}/") as resp:
            answer = await resp.text()
            data = json.loads(answer)
            # print(data)
            ikb_task = generate_ikb_list_tasks(data)
            amount_tasks = len(data)
            await message.answer(text=f"Список задач ({amount_tasks} шт.):",
                                 parse_mode="HTML",
                                 reply_markup=ikb_task)
            await message.delete()


async def list_delete(message: types.Message, state: FSMContext):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{URL}/tg/list_tasks/{message.from_user.id}/") as resp:
            answer = await resp.text()
            data = json.loads(answer)
            ikb_task = generate_ikb_list_tasks_delete(data)
            amount_tasks = len(data)
            await message.answer(text=f"Список задач ({amount_tasks} шт.):",
                                 parse_mode="HTML",
                                 reply_markup=ikb_task)
            await message.delete()
            async with state.proxy() as data:
                data['user_id'] = message.from_user.id
                data['message_id'] = message.message_id
            await FSMClientDelTask.user_id.set()


async def callback_choice_task_delete(callback: types.CallbackQuery, state: FSMContext):
    task_id = callback.data[callback.data.find('_') + 1:]
    title = ''
    await callback.answer()
    tasks = callback.message.reply_markup.inline_keyboard
    for task in tasks:
        if callback.data == task[0]['callback_data']:
            title = task[0]['text']

    await callback.message.edit_text(text=f'Вы уверены, что хотите удалить?\n\n'
                                          f'<strong>{title}</strong>',
                                     reply_markup=ikb_yes_no,
                                     parse_mode='HTML')

    async with state.proxy() as data:
        data['task_id'] = task_id
        data['task_title'] = title
    await FSMClientDelTask.next()
    await FSMClientDelTask.next()
    await FSMClientDelTask.next()
    await FSMClientDelTask.next()


async def callback_confirm_delete(callback: types.CallbackQuery, state: FSMContext):
    confirm = callback.data[callback.data.find('btn_confirm_') + 12:]
    await callback.answer()
    async with state.proxy() as data:
        data['confirm'] = confirm
        if confirm == 'yes':
            print(confirm)
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{URL}/tg/del_tasks/{data['task_id']}/") as resp:
                    answer = await resp.text()
                    task = json.loads(answer)
                    await callback.message.edit_text(text=get_msg_delete_task(title=task['title'],
                                                                              type_id=task['type_id'],
                                                                              type_title=task['type_title'],
                                                                              number=task['number'],
                                                                              date=task['date']
                                                                              ),
                                                     parse_mode='HTML')
        else:
            await callback.message.delete()
    await FSMClientDelTask.next()
    await state.finish()


async def settings(message: types.Message):
    btn_name = InlineKeyboardButton(text='Наименование', callback_data='btn_settings_name')
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(btn_name)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'⚙️ Настройки бота:\n',
                           parse_mode="HTML",
                           reply_markup=ikb)
    await message.delete()


async def get_text_settings_name(mode: bool) -> str:
    if mode:
        return f'Если выключить опцию, то наименование МИ будет в следующем формате.\n\n' \
               f'<i>Например:</i>\nКатетеры (РУ)'
    return f'Если включить опцию, то наименование МИ будет в следующем формате.\n\n' \
           f'<i>Например:</i>\nКатетеры (РУ | Вх. № 12345 от 01.01.2021)'


async def callback_settings_name(callback: types.CallbackQuery):
    tg_chat_id = callback.from_user.id
    text = ''
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{URL}/tg/users/{tg_chat_id}/task_detail/") as resp:
            response = json.loads(await resp.text())
            result: str = response['task_title_detail']
            btn_name = InlineKeyboardButton(text='Вкл.', callback_data='btn_settings_on')
            if result.lower() == 'true':
                btn_name.text = 'Выкл.'
                btn_name.callback_data = 'btn_settings_off'
                text = await get_text_settings_name(True)
            elif result.lower() == 'false':
                btn_name.text = 'Вкл.'
                btn_name.callback_data = 'btn_settings_on'
                text = await get_text_settings_name(False)
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(btn_name)
    await callback.answer()
    await callback.message.edit_text(text=text,
                                     reply_markup=ikb,
                                     parse_mode='HTML')


async def callback_settings_name_on(callback: types.CallbackQuery):
    tg_chat_id = callback.from_user.id
    btn_name_off = InlineKeyboardButton(text='Выкл.', callback_data='btn_settings_off')
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(btn_name_off)
    await callback.answer('Изменения сохранены')
    # await callback.message.edit_text(text=await get_text_settings_name(True),
    #                                  reply_markup=ikb,
    #                                  parse_mode='HTML')
    data = {
        "task_title_detail": True
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://{URL}/tg/users/{tg_chat_id}/task_detail/", data=data) as resp:
            response = await resp.text()
    await callback.message.delete()


async def callback_settings_name_off(callback: types.CallbackQuery):
    tg_chat_id = callback.from_user.id
    btn_name_on = InlineKeyboardButton(text='Вкл.', callback_data='btn_settings_on')
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(btn_name_on)
    await callback.answer('Изменения сохранены')
    data = {
        "task_title_detail": False
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://{URL}/tg/users/{tg_chat_id}/task_detail/", data=data) as resp:
            response = await resp.text()
    await callback.message.delete()
    # await callback.message.edit_text(text=await get_text_settings_name(False),
    #                                  reply_markup=ikb,
    #                                  parse_mode='HTML')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(add_task, commands=['add'], state=None)
    dp.register_message_handler(updates, commands=['updates'])
    dp.register_message_handler(list_tasks, commands=['list'])
    dp.register_message_handler(settings, commands=['settings'])
    dp.register_message_handler(list_delete, commands=['delete'])
    dp.register_callback_query_handler(callback_type,
                                       lambda callback_query: callback_query.data.startswith('type_'),
                                       state=FSMClientAddTask.type)
    dp.register_callback_query_handler(callback_choice_task_delete,
                                       lambda callback_query: callback_query.data.startswith('del_'),
                                       state=FSMClientDelTask.user_id)
    dp.register_callback_query_handler(callback_confirm_delete,
                                       lambda callback_query: callback_query.data.startswith('btn_confirm_'),
                                       state=FSMClientDelTask.confirm)
    dp.register_message_handler(add_name_md, state=FSMClientAddTask.name_md)
    dp.register_message_handler(add_number, state=FSMClientAddTask.number)
    dp.register_message_handler(add_date, state=FSMClientAddTask.date)
    dp.register_callback_query_handler(callback_settings_name,
                                       lambda callback_query: callback_query.data == 'btn_settings_name')
    dp.register_callback_query_handler(callback_settings_name_on,
                                       lambda callback_query: callback_query.data == 'btn_settings_on')
    dp.register_callback_query_handler(callback_settings_name_off,
                                       lambda callback_query: callback_query.data == 'btn_settings_off')
    dp.register_callback_query_handler(callback_cansel, lambda callback_query: callback_query.data == 'btn_cansel',
                                       state='*')
