from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keboard.keyboards import get_keyboard_1, get_keyboard_2
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)




keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton('Кнопка 1')
button_2 = KeyboardButton('Кнопка 2')
button_3 = KeyboardButton('Отправь фото кота')
button_4 = KeyboardButton('Перейти на следующую клавиатуру')
keyboard.add(button_1, button_2, button_3, button_4)

keyboard_2= ReplyKeyboardMarkup(resize_keyboard=True)
button_5 = KeyboardButton('Отправь фото хомяка')
button_6 = KeyboardButton('Вернуться на 1 клавиатуру')
keyboard_2.add(button_5, button_6)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Кнопка 1')
async def button_1_click(message: types.Message):
    await message.answer('Ты нажал кнопку 1')


@dp.message_handler(lambda message: message.text == 'Кнопка 2')
async def button_2_click(message: types.Message):
    await message.answer('Ты нажал кнопку 2')

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://icdn.lenta.ru/images/2023/11/28/16/20231128163903784/square_1280_283df4079b9b28cab0e06492462f760a.jpeg', caption='Вот тебе кошка')


@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото хомяка', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Кнопка 4')
async def button_4_click(message: types.Message):
    await message.answer('Ты нажал кнопку 2')

@dp.message_handler(lambda message: message.text == 'Отправь фото хомяка')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://zoolike.by/image/cache/data/from_url/v-nashem-dome-poselilsya-zamechatelnyj-homyak-170104102151-906698009503420-49444-500x500.jpg')

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото  кошки', reply_markup=get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)