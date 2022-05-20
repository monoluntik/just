import logging
from test import get_total
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
API_TOKEN = '5283215952:AAEhuPpI5rosTD3U3VM3I2kBO80ADCWzy9w'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    hk = get_total(message.text)
    await message.answer(f'{hk}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)