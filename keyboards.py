import types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from bot_creation import *
from data.database import *
from StatesGroups import *
from data.database import *


cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cancel_markup.add(KeyboardButton('/cancel'))

b1 = InlineKeyboardButton('Софты', callback_data='Софты')
b2 = InlineKeyboardButton('Канал', url='https://t.me/AT_industries')
menu_markup = InlineKeyboardMarkup()
menu_markup.add(b1, b2)

promocode_check_markup = InlineKeyboardMarkup()
b1 = InlineKeyboardButton('Пропустить', callback_data='skip_promocode')
b2 = InlineKeyboardButton('🔺 Отменить покупку', callback_data='%Назад Софт')
promocode_check_markup.add(b1).add(b2)

cancel_purchase_markup = InlineKeyboardMarkup()
b1 = InlineKeyboardButton('🔺 Отменить покупку', callback_data='cancel_purchase_callback')
cancel_purchase_markup.add(b1)

@dp.callback_query_handler(lambda call: call.data.startswith('cancel_purchase_callback'))
async def cancel_purchase(callback: types.CallbackQuery):
    pass


@dp.callback_query_handler(lambda call: call.data.startswith('skip_promocode'))
async def skip_promocode(callback: types.CallbackQuery, state: FSMContext):
    price = '7777'
    await callback.answer('')
    await PaymentStatesGroup.transaction_verification.set()
    await bot.send_message(chat_id=callback.message.chat.id,
                                text=f'Переведите {price} USDT по адресу: ХХХХХХХХХХХХХХХХХХХХХХ и отправьте идентификатор транзакции',
                                parse_mode='markdown', reply_markup=cancel_purchase_markup)

@dp.message_handler(state=PaymentStatesGroup.transaction_verification)
async def transaction_verification(message: types.Message, state: FSMContext):
    if message.text == message.text:
        await message.answer('Транзакция подтверждена, пришлите ссылку на свой гитхаб', reply_markup=cancel_purchase_markup)
    await PaymentStatesGroup.github.set()

@dp.message_handler(state=PaymentStatesGroup.github)
async def github(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['github'] = message.text
    await message.answer(f"Покупка софта: <u><b>{data['soft_name']}</b></u> за <u><b>{data['soft_price']} USDT</b></u> успешно совершена. Доступ к проекту будет открыт в течении 4х часов", parse_mode='html')
    DataBase.addpurchase(user_id=message.from_user.id, username=message.from_user.first_name+' '+message.from_user.last_name, user_github=['github'], soft_name=['soft_name'], soft_price=['soft_price'], refer_id='REFERIDIDIDIDIDI', refer_discount=989898, promocode='promo', discount=8888, total_discount=5555, purchased=11111)
    await state.finish()

@dp.callback_query_handler(lambda call: call.data.startswith('do_not_have_a_promocode'))
async def back_to_soft_consideration_button(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer('⚙️⚙️⚙️')
    '''await PaymentStatesGroup.promocode2.set()
    await bot.send_message(chat_id=callback.message.chat.id,
                                text='*Введите промокод*',
                                parse_mode='markdown', reply_markup=cancel_markup)
'''


@dp.callback_query_handler(lambda call: call.data.startswith('%Назад Софт'))
async def back_to_soft_consideration_button(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='*Добро пожаловать, выберите, что вам нужно в меню ниже!*',
                                parse_mode='markdown', reply_markup=menu_markup)


@dp.callback_query_handler(lambda call: call.data.startswith('Софты'))
async def soft_key_board(callback: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='*Выберите софт, чтобы узнать более подробную информацию о нем!*',
                                parse_mode='markdown', reply_markup=get_softs_inlinekeyboard())



b1 = InlineKeyboardButton('Купить', callback_data='Купить')
@dp.callback_query_handler(lambda call: call.data.startswith('Купить'))
async def buy_callback(callback: types.CallbackQuery, state: FSMContext):
    soft_name = (callback.message.text).split('\n')[0][10::]
    soft_price = (callback.message.text).split('\n')[4].split()[1]
    async with state.proxy() as data:
        data['soft_name'] = soft_name
        data['soft_price'] = soft_price
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Введите промокод или нажмите "пропустить"', reply_markup=promocode_check_markup)

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