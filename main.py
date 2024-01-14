import asyncio
import logging

import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession

logging.basicConfig(level=logging.INFO)

session = AiohttpSession(proxy='http://proxy.server:3128')
bot = Bot(token=os.getenv("TOOSA_BOT_TOKEN"), session=session)
dp = Dispatcher()


@dp.message(F.new_chat_members)
async def delete_new_member_msg(message: Message):
    await message.delete()


@dp.message(F.left_chat_member)
async def delete_left_member_msg(message: Message):
    await message.delete()


async def main():
    await dp.start_polling(bot)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(main())
