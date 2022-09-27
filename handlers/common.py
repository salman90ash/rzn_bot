import asyncio

import aiohttp

from bot import bot
from aiogram import types, Dispatcher


# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.post('http://127.0.0.1:8000/tg/') as resp:
#             print(resp.status)
#             print(await resp.text())



# async def echo(message: types.Message):
#     text = message.text
#     send_msg = await bot.send_message(chat_id=message.from_user.id, text=text, parse_mode='HTML')
#     await message.delete()
#     await main()


def register_handlers_common(dp: Dispatcher):
    pass
    # dp.register_message_handler(echo)
