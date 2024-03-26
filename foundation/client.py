from aiogram import types
from create_bot import *
import keyboards as kb

"""#################################  # # # # # # # # # # # # # ######################################"""
"""######################### # # # #       MAIN FUNCTIONS       # # # # ##############################"""
"""#################################  # # # # # # # # # # # # # ######################################"""

# @dp.message_handler(commands=['start'])
async def startf(message: types.Message):
    await message.delete()
    await message.answer("*Здравствуйте! Нажмите на /menu, чтобы начать работу с ботом*", parse_mode='markdown')
    # добавляем\проверяем пользователя в БД
    user_id = message.from_user.id
    name = message.from_user.first_name
    data_base.adduser(user_id, name, message)




# @dp.message_handler(commands=['menu'])
async def menuf(message: types.Message):
    await message.answer(f'*Добро пожаловать!*',
                         parse_mode='markdown',
                         reply_markup=kb.menu_markup)


# @dp.message_handler()

async def main_function(message: types.Message):
    await message.reply('ответ на сообщение не по шаблону!')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(startf, commands=['start'])
    dp.register_message_handler(menuf, commands=['menu'])
    dp.register_message_handler(main_function)
