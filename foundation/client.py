from aiogram import types
from bot_creation import *
import keyboards as kb
from data.TEXT import *
async def cmd_state_cancel(message, state):
    msg = message.text
    if msg in CMDS_CLIENT:
        await state.finish()
        if msg == CMD_START:
            startf(message)
        if msg == CMD_MENU:
            menuf(message)
        return True
    return False

"""#################################  # # # # # # # # # # # # # ######################################"""
"""######################### # # # #       MAIN FUNCTIONS       # # # # ##############################"""
"""#################################  # # # # # # # # # # # # # ######################################"""

# @dp.message_handler(commands=['start'])
async def startf(message: types.Message):
    await message.delete()
    await message.answer(MSG['RUS']['ADMIN']['MSG_START'], parse_mode='markdown')
    # добавляем\проверяем пользователя в БД
    user_id = message.from_user.id
    name = message.from_user.first_name
    data_base.adduser(user_id, name, message)


# @dp.message_handler(commands=['menu'])
async def menuf(message: types.Message):
    await message.answer(MSG['RUS']['ADMIN']['MSG_MENU'],
                         parse_mode='markdown',
                         reply_markup=kb.menu_markup)


# @dp.message_handler()

async def main_function(message: types.Message):
    await message.reply(MSG['RUS']['STATES']['OTHERWISE'])


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(startf, commands=['start'])
    dp.register_message_handler(menuf, commands=['menu'])
    dp.register_message_handler(main_function)
