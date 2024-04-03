from bot_creation import *
from aiogram import types
import keyboards as kb

"""#################################  # # # # # # # # # # # # # ######################################"""
"""########################### # # # #       CALL BACK       # # # # #################################"""
"""#################################  # # # # # # # # # # # # # ######################################"""
'''

# @dp.callback_query_handler()
async def callback_func(callback: types.CallbackQuery):
    # if callback.data == 'Софты':
        # await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='*Выберите софт, чтобы узнать более подробную информацию о нем!*', parse_mode='markdown', reply_markup=kb.get_softs_inlinekeyboard())
    if callback.data == 'Купить':
        await callback.answer('⚠️  ОПЛАТА ВРЕМЕННО НЕДОСТУПНА  ⚠️')
    elif callback.data == "Назад Меню":
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='*Добро пожаловать, выберите, что вам нужно в меню ниже!*', parse_mode='markdown', reply_markup=kb.menu_markup)
    elif callback.data == "Назад Покупка":
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='*Выберите софт, чтобы узнать более подробную информацию о нем!*', parse_mode='markdown', reply_markup=kb.get_softs_inlinekeyboard())
    elif '&&&' == callback.data[:3]:
        data_base.delpartner(callback.data[3:])
        await callback.message.edit_reply_markup(reply_markup=kb.get_partners_inlinekeyboard_4delete())
    elif '$$$' == callback.data[:3]:
        data_base.delsoft(callback.data[3:])
        await callback.message.edit_reply_markup(reply_markup=kb.get_softs_inlinekeyboard_4delete())
    else:
        data_list = data_base.select_software_info(callback.data)[0]
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=f'<b><u>Название</u>:</b> {data_list[0]}\n\n<b><u>Описание</u>:</b> {data_list[1]}\n\n<b><u>Цена</u>:</b> {data_list[2]} USDT', parse_mode='html', reply_markup=kb.soft_consideration)


def register_handlers_callback(dp : Dispatcher):
    dp.register_callback_query_handler(callback_func)
'''