from shortcut import get_type_title
from bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.ikb import ikb_type, ikb_cansel
# from rzn.functions.actions import get_type_title, add_task
# from users.models import CustomUser
import asyncio
import aiohttp


class FSMClient(StatesGroup):
    type = State()
    user_id = State()
    message_id = State()
    name_md = State()
    number = State()
    date = State()


async def create_user(data):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8000/tg/create_user/', data=data) as resp:
            # print(resp.status)
            print(await resp.text())


async def create_task(data):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8000/tg/create_task/', data=data) as resp:
            # print(resp.status)
            print(await resp.text())


def get_template_message(type_id, name_md='???', number='???', date='???') -> str:
    global RZN_TYPES
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


start_message = f"Добро пожаловать!\n" \
                f"Для взаимодействия с ботом используйте команды.\n" \
                f"Бот не работает в групповых чатах.\n" \
                f"За новостями и о статусе работы бота можно следить на канале [regassistant](https://t.me/regassistant). " \
                f"Также на канале можно оставить комментарий, если есть проблема/пожелание\n"


async def start(message: types.Message):
    await message.answer(text=start_message, parse_mode='Markdown')
    user = {
        "user_id": message.from_user.id
    }
    if message.from_user.username is not None:
        user['username'] = message.from_user.username
    if message.from_user.first_name is not None:
        user['first_name'] = message.from_user.first_name
    if message.from_user.last_name is not None:
        user['last_name'] = message.from_user.last_name
    # print(user)
    await create_user(user)
    # print(message.as_json())
    await message.delete()


async def add_task(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Выберите тип задачи', parse_mode="HTML",
                           reply_markup=ikb_type)
    await message.delete()
    await FSMClient.type.set()


async def callback_type(callback: types.CallbackQuery, state: FSMContext):
    type_id = callback.data[callback.data.find('_') + 1:]
    async with state.proxy() as data:
        data['message_id'] = callback.message.message_id
        data['user_id'] = callback.message.from_user.id
        data['type'] = type_id
    await callback.answer()
    await callback.message.edit_text(text=get_template_message(type_id=type_id),
                                     reply_markup=ikb_cansel,
                                     parse_mode='HTML')
    await FSMClient.next()
    await FSMClient.next()
    await FSMClient.next()


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
                                    text=get_template_message(type_id=data['type'],
                                                              name_md=data['name_md']),
                                    reply_markup=ikb_cansel,
                                    parse_mode='HTML')
    await FSMClient.next()
    await message.delete()


async def add_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        await bot.edit_message_text(message_id=data['message_id'],
                                    chat_id=message.from_user.id,
                                    text=get_template_message(type_id=data['type'],
                                                              name_md=data['name_md'],
                                                              number=data['number']),
                                    reply_markup=ikb_cansel,
                                    parse_mode='HTML')
    await FSMClient.next()
    await message.delete()


async def add_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
        await bot.edit_message_text(message_id=data['message_id'],
                                    chat_id=message.from_user.id,
                                    text=get_template_message(type_id=data['type'],
                                                              name_md=data['name_md'],
                                                              number=data['number'],
                                                              date=data['date']),
                                    parse_mode='HTML')
    await FSMClient.next()
    await message.delete()
    # print(data.as_dict())
    await create_task(data.as_dict())
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(add_task, commands=['add'], state=None)
    dp.register_callback_query_handler(callback_type, lambda callback_query: callback_query.data.startswith('type_'),
                                       state=FSMClient.type)
    dp.register_message_handler(add_name_md, state=FSMClient.name_md)
    dp.register_message_handler(add_number, state=FSMClient.number)
    dp.register_message_handler(add_date, state=FSMClient.date)
    dp.register_callback_query_handler(callback_cansel, lambda callback_query: callback_query.data == 'btn_cansel',
                                       state='*')
