# import asyncio
import asyncio
import datetime

from aiogram import executor
from bot import dp
from handlers import client, common
import aioschedule as schedule
from handlers.common import send_msg

client.register_handlers_client(dp)
common.register_handlers_common(dp)


async def time():
    print(datetime.datetime.now())


async def scheduler():
    # schedule.every().day.at("08:00").do(send_msg)
    # schedule.every().day.at("11:00").do(send_msg)
    # schedule.every().day.at("14:00").do(send_msg)
    # schedule.every().day.at("17:00").do(send_msg)
    # schedule.every().day.at("20:00").do(send_msg)
    schedule.every(15).minutes.do(time)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    print('bot activated')
    print(datetime.datetime.now())
    asyncio.create_task(scheduler())
    # schedule.every().day.at('16:47').do(time)
    # # schedule.every().day.at('16:44').do(send_msg)
    # while True:
    #     await schedule.run_pending()


if __name__ == "__main__":
    # from rzn.tg.handlers.common import dp
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
