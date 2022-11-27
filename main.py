# import asyncio
import asyncio
import datetime
from aiogram import executor
from bot import dp
from handlers import client, common
import aioschedule as schedule
from handlers.common import send_msg
from handlers.client import updates

client.register_handlers_client(dp)
common.register_handlers_common(dp)


async def time():
    print(datetime.datetime.now())


async def scheduler():
    # print('start_scheduler')
    schedule.every().day.at("08:00").do(updates, '')
    schedule.every().day.at("09:00").do(updates, '')
    schedule.every().day.at("10:00").do(updates, '')
    schedule.every().day.at("11:00").do(updates, '')
    schedule.every().day.at("12:00").do(updates, '')
    schedule.every().day.at("13:00").do(updates, '')
    schedule.every().day.at("14:00").do(updates, '')
    schedule.every().day.at("15:00").do(updates, '')
    schedule.every().day.at("16:00").do(updates, '')
    schedule.every().day.at("17:00").do(updates, '')
    schedule.every().day.at("18:00").do(updates, '')
    schedule.every().day.at("19:00").do(updates, '')
    schedule.every().day.at("20:00").do(updates, '')
    schedule.every().day.at("21:02").do(updates, '')
    # schedule.every(15).minutes.do(time)
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
