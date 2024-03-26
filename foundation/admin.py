from aiogram import types
from aiogram.dispatcher import FSMContext
from create_bot import *
import keyboards as kb
from StatesGroups import *
from config import admin_id
from create_bot import cancel_check

# ##################################################################################################### #
# ############################################# ADMIN ################################################# #
# ##################################################################################################### #

"""#################################  # # # # # # # # # # # # # ######################################"""
"""############################## # # # #       SOFT       # # # # ###################################"""
"""#################################  # # # # # # # # # # # # # ######################################"""
# ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD


# @dp.message_handler(commands=['addsoft'], state=None)
async def start_work(message: types.Message):
    if message.from_user.id in admin_id:
        await ClientStatesGroup.name.set()
        await message.answer('*Сначала отправь название софта, который хочешь добавить*',
                             parse_mode='markdown',
                             reply_markup=kb.cancel_markup)
    else:
        await message.reply('*У вас нет прав на использование этой команды!*', parse_mode='markdown')


# @dp.message_handler(lambda message: message.text, state=ClientStatesGroup.name)
async def load_softname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await ClientStatesGroup.next()
    await message.reply('*А теперь отправь описание*', parse_mode='markdown')


# @dp.message_handler(state=ClientStatesGroup.desc)
async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
    await ClientStatesGroup.next()
    await message.reply('*Теперь отправь цену софта*', parse_mode='markdown')


# @dp.message_handler(state=ClientStatesGroup.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    data_base.addsoft(name=data['name'], desc=data['desc'], price=data['price'])
    await message.reply(f'*База Данных была обновлена: софт был добавлен*', parse_mode='markdown')
    await state.finish()


# DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE
# @dp.message_handler(commands=['delsoft'])
async def delete_soft(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer('*Выберите софт, который хотите удалить*', reply_markup=kb.get_softs_inlinekeyboard_4delete(), parse_mode='markdown')
    else:
        await message.reply('*У вас нет прав на использование этой команды!*', parse_mode='markdown')


"""#################################  # # # # # # # # # # # # # ######################################"""
"""############################# # # # #       PARTNER       # # # # #################################"""
"""#################################  # # # # # # # # # # # # # ######################################"""

# ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD


# @dp.message_handler(commands=['addpartner'])
async def add_partner(message: types.Message):
    if message.from_user.id in admin_id:
        await PartnerStatesGroup.user_id.set()
        await message.answer('*Сначала отправь id партнера, которого хочешь добавить*',
                             parse_mode='markdown',
                             reply_markup=kb.cancel_markup)
    else:
        await message.reply('*У вас нет прав на использование этой команды!*', parse_mode='markdown')

# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.user_id)
async def load_userid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.text
    await PartnerStatesGroup.name.set()
    await message.reply('*Теперь введите имя партнера*', reply_markup=kb.cancel_markup, parse_mode='markdown')

# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.name)
async def load_partnername(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await PartnerStatesGroup.promocode.set()
    await message.reply('*введите промокод партнера*', reply_markup=kb.cancel_markup, parse_mode='markdown')


# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.promocode)
async def load_promo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['promocode'] = message.text
    await PartnerStatesGroup.discount.set()
    await message.reply('*введите размер скидки промокода*', reply_markup=kb.cancel_markup, parse_mode='markdown')


# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.discount)
async def load_discount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['discount'] = message.text
    await PartnerStatesGroup.quantity.set()
    await message.reply('*введите кол-во промокодов*', reply_markup=kb.cancel_markup, parse_mode='markdown')


# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.quantity)
async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text
    data_base.addpartner(data['user_id'], data['name'], data['promocode'], data['discount'], data['quantity'])
    await state.finish()
    await message.reply('*База данных обновлена: партнер был добавлен*', parse_mode='markdown')


# DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE

# @dp.message_handler(commands=['delpartner'], state=None)
async def delete_partner(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer('*Выбери партнера, которого хочешь удалить из базы данных*',
                             parse_mode = 'markdown',
                             reply_markup=kb.get_partners_inlinekeyboard_4delete())
    else:
        await message.reply('*У вас нет прав на использование этой команды!*', parse_mode='markdown')

"""#################################  # # # # # # # # # # # # # ######################################"""
"""############################ # # # #       REFRESH       # # # # ##################################"""
"""#################################  # # # # # # # # # # # # # ######################################"""


# @dp.message_handler(commands=['refresh'])
'''async def refresh_func(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer('*Выберите, какую базу данных вы хотите обновить*', reply_markup=kb.refresh_markup, parse_mode='markdown')
    else:
        await message.reply('*У вас нет прав на использование этой команды!*', parse_mode='markdown')'''


"""#################################  # # # # # # # # # # # # # ######################################"""
"""########################### # # # #       ADMIN HELP       # # # # ################################"""
"""#################################  # # # # # # # # # # # # # ######################################"""


# @dp.message_handler(commands=['admin_help'])
async def admin_help(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer("""
*/addsoft* - _добавить софт в бд_
*/delsoft* - _удалить софт из бд_
*/addpartner* - _добавить партнера в бд_
*/delpartner* - _удалить партнера из бд_
*/refresh* - _отчистить одну из таблиц бд_
        """, parse_mode='markdown')
    else:
        await message.reply('*У вас нет прав на использование этой команды!*', parse_mode='markdown')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(start_work, commands=['addsoft'])
    dp.register_message_handler(load_softname, lambda message: message.text, state=ClientStatesGroup.name)
    dp.register_message_handler(load_desc, state=ClientStatesGroup.desc)
    dp.register_message_handler(load_price, state=ClientStatesGroup.price)
    dp.register_message_handler(delete_soft, commands=['delsoft'])
    dp.register_message_handler(add_partner, commands=['addpartner'], state=None)
    dp.register_message_handler(load_userid, state=PartnerStatesGroup.user_id)
    dp.register_message_handler(load_partnername, state=PartnerStatesGroup.name)
    dp.register_message_handler(load_promo, state=PartnerStatesGroup.promocode)
    dp.register_message_handler(load_discount, state=PartnerStatesGroup.discount)
    dp.register_message_handler(load_quantity, state=PartnerStatesGroup.quantity)
    dp.register_message_handler(delete_partner, commands=['delpartner'], state=None)
    # dp.register_message_handler(refresh_func, commands=['refresh'])
    dp.register_message_handler(admin_help, commands=['admin_help'])

