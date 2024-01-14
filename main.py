import asyncio
import logging

import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("TOOSA_BOT_TOKEN"))
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
