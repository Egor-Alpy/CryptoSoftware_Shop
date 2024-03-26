from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3 as sq


cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cancel_markup.add(KeyboardButton('/cancel'))

b1 = InlineKeyboardButton('Софты', callback_data='Софты')
b2 = InlineKeyboardButton('Канал', url='https://t.me/AT_industries')
menu_markup = InlineKeyboardMarkup()
menu_markup.add(b1, b2)

b1 = InlineKeyboardButton('software', callback_data='software')
b2 = InlineKeyboardButton('users', callback_data='users')
b3 = InlineKeyboardButton('partners', callback_data='partners')
refresh_markup = InlineKeyboardMarkup()
refresh_markup.add(b1, b2, b3)

b1 = InlineKeyboardButton('Купить', callback_data='Купить')
b2 = InlineKeyboardButton('🔺 Назад', callback_data='Назад Покупка')
soft_consideration = InlineKeyboardMarkup()
soft_consideration.add(b1, b2)


# ++++++++++++++++++++++++++++++++++++++++++++++ MARKUP FUNCTIONS +++++++++++++++++++++++++++++++++++++++++++++++++++++


def get_softs_inlinekeyboard():
    with sq.connect("shop3_0.db") as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM software")
        rows = cur.fetchall()
        softs_markup = InlineKeyboardMarkup()
        for i in range(len(rows)):
            softs_markup.add(InlineKeyboardButton(rows[i][0], callback_data=rows[i][0]))

        softs_markup.add(InlineKeyboardButton('🔺 Назад', callback_data='Назад'))
        return softs_markup


def get_softs_inlinekeyboard_4delete():
    with sq.connect("shop3_0.db") as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM software")
        rows = cur.fetchall()
        softs_markup = InlineKeyboardMarkup()
        for i in range(len(rows)):
            softs_markup.add(InlineKeyboardButton(rows[i][0], callback_data='$$$' + rows[i][0]))
        return softs_markup


def get_partners_inlinekeyboard_4delete():
    with sq.connect("shop3_0.db") as con:
        cur = con.cursor()
        cur.execute("SELECT user_id, name, promocode, discount, quantity FROM partners")
        rows = cur.fetchall()
        partners_markup = InlineKeyboardMarkup()
        for i in range(len(rows)):
            partners_markup.add(InlineKeyboardButton(f"name: {rows[i][1]}|id: {rows[i][0]}|promo: {rows[i][2]}|disc: {rows[i][3]}USDT|qty: {rows[i][4]}", callback_data='&&&' + rows[i][0]))
        return partners_markup