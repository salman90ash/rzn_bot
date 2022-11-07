from aiogram import types, Dispatcher
from bot import bot
from config import ADMIN_ID


async def inbox(message: types.Message):
    text = message.text
    send_msg = await bot.send_message(chat_id=message.from_user.id, text=text, parse_mode='HTML')
    print(message)
    # await message.delete()
    # await main()


async def send_msg():
    msg = await bot.send_message(chat_id=ADMIN_ID, text='text', parse_mode='HTML')
    print(msg)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(inbox)
