from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3 as sq
from bot_creation import *
from aiogram import types
from data.database import *


cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cancel_markup.add(KeyboardButton('/cancel'))

b1 = InlineKeyboardButton('Софты', callback_data='Софты')
b2 = InlineKeyboardButton('Канал', url='https://t.me/AT_industries')
menu_markup = InlineKeyboardMarkup()
menu_markup.add(b1, b2)
@dp.callback_query_handler(lambda call: call.data.startswith('Софты'))
async def soft_key_board(callback: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='*Выберите софт, чтобы узнать более подробную информацию о нем!*',
                                parse_mode='markdown', reply_markup=get_softs_inlinekeyboard())



b1 = InlineKeyboardButton('Купить', callback_data='Купить')
@dp.callback_query_handler(lambda call: call.data.startswith('Купить'))
async def buy_callback(callback: types.CallbackQuery):
    await callback.answer('⚠️  ОПЛАТА ВРЕМЕННО НЕДОСТУПНА  ⚠️')

b2 = InlineKeyboardButton('🔺 Назад', callback_data='Назад Покупка')
@dp.callback_query_handler(lambda call: call.data.startswith('Назад Покупка'))
async def back_from_description_menu(callback: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='*Выберите софт, чтобы узнать более подробную информацию о нем!*',
                                parse_mode='markdown', reply_markup=get_softs_inlinekeyboard())


soft_consideration = InlineKeyboardMarkup()
soft_consideration.add(b1, b2)


# ++++++++++++++++++++++++++++++++++++++++++++++ MARKUP FUNCTIONS +++++++++++++++++++++++++++++++++++++++++++++++++++++


def get_softs_inlinekeyboard():
    with sq.connect("db_atshop.db") as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM software")
        rows = cur.fetchall()
        softs_markup = InlineKeyboardMarkup()
        for i in range(len(rows)):
            softs_markup.add(InlineKeyboardButton(rows[i][0], callback_data='SOFT'+rows[i][0]))

        softs_markup.add(InlineKeyboardButton('🔺 Назад', callback_data='Назад Меню'))
        return softs_markup
@dp.callback_query_handler(lambda call: call.data.startswith('Назад Меню'))
async def back_from_soft_menu(callback: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='*Добро пожаловать, выберите, что вам нужно в меню ниже!*', parse_mode='markdown',
                                reply_markup=menu_markup)


def get_softs_inlinekeyboard_4delete():
    with sq.connect("db_atshop.db") as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM software")
        rows = cur.fetchall()
        softs_markup = InlineKeyboardMarkup()
        for i in range(len(rows)):
            softs_markup.add(InlineKeyboardButton(rows[i][0], callback_data='$$$' + rows[i][0]))
        return softs_markup
@dp.callback_query_handler(lambda call: call.data.startswith('$$$'))
async def software_list_menu(callback: types.CallbackQuery):
    data_base.delsoft(callback.data[3:])
    await callback.message.edit_reply_markup(reply_markup=get_softs_inlinekeyboard_4delete())


def get_partners_inlinekeyboard_4delete():
    with sq.connect("db_atshop.db") as con:
        cur = con.cursor()
        cur.execute("SELECT user_id, name, promocode, discount, quantity FROM partners")
        rows = cur.fetchall()
        partners_markup = InlineKeyboardMarkup()
        for i in range(len(rows)):
            partners_markup.add(InlineKeyboardButton(f"name: {rows[i][1]}|id: {rows[i][0]}|promo: {rows[i][2]}|disc: {rows[i][3]}USDT|qty: {rows[i][4]}", callback_data='&&&' + str(rows[i][0])))
        return partners_markup
@dp.callback_query_handler(lambda call: call.data.startswith('&&&'))
async def admin_info_keyboard(callback: types.CallbackQuery):
    data_base.delpartner(callback.data[3:])
    await callback.message.edit_reply_markup(reply_markup=get_partners_inlinekeyboard_4delete())

@dp.callback_query_handler(lambda call: call.data.startswith('SOFT'))
async def chosen_soft(callback: types.CallbackQuery):
    data_list = data_base.select_software_info(callback.data[4:])[0]
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text=f'<b><u>Название</u>:</b> {data_list[0]}\n\n<b><u>Описание</u>:</b> {data_list[1]}\n\n<b><u>Цена</u>:</b> {data_list[2]} USDT',
                                parse_mode='html', reply_markup=soft_consideration)