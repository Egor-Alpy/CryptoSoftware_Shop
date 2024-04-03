from bot_creation import *
import keyboards as kb
from StatesGroups import *
from config import admin_id
from other import is_number
from data.TEXT import *
# ##################################################################################################### #
# ############################################# ADMIN ################################################# #
# ##################################################################################################### #

# Остановка машины состояния при вызове новой команды и вызов этой команды
async def cmd_state_cancel_admin(message, state):
    msg = message.text
    if msg in CMDS_ADMIN:
        await state.finish()

        if msg == CMD_DEL_SOFT:
            await delete_soft(message)
        if msg == CMD_ADD_SOFT:
            await add_soft(message)
        if msg == CMD_DEL_PARTNER:
            await delete_partner(message)
        if msg == CMD_ADD_PARTNER:
            await add_partner(message)
        return True
    return False

"""#################################  # # # # # # # # # # # # # ######################################"""
"""############################## # # # #       SOFT       # # # # ###################################"""
"""#################################  # # # # # # # # # # # # # ######################################"""
# ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD


# @dp.message_handler(commands=['addsoft'], state=None)
async def add_soft(message: types.Message):
    if message.from_user.id in admin_id:
        await ClientStatesGroup.name.set()
        await message.answer(MSG['RUS']['STATES']['SOFT']['NAME'],
                             parse_mode='markdown',
                             reply_markup=kb.cancel_markup)
    else:
        await message.reply(MSG['RUS']['STATES']['MISTAKE']['NO ROOTS'], parse_mode='markdown')


# @dp.message_handler(lambda message: message.text, state=ClientStatesGroup.name)
async def load_softname(message: types.Message, state: FSMContext):
    if await cmd_state_cancel_admin(message, state):
        return
    async with state.proxy() as data:
        data['name'] = message.text
    await ClientStatesGroup.next()
    await message.reply(MSG['RUS']['STATES']['SOFT']['DESC'], parse_mode='markdown')


# @dp.message_handler(state=ClientStatesGroup.desc)
async def load_desc(message: types.Message, state: FSMContext):
    if await cmd_state_cancel_admin(message, state):
        return
    async with state.proxy() as data:
        data['desc'] = message.text
    await ClientStatesGroup.next()
    await message.reply(MSG['RUS']['STATES']['SOFT']['PRICE'], parse_mode='markdown')


# @dp.message_handler(state=ClientStatesGroup.price)
async def load_price(message: types.Message, state: FSMContext):
    if await cmd_state_cancel_admin(message, state):
        return
    if is_number(message.text):
        async with state.proxy() as data:
            data['price'] = message.text
        data_base.addsoft(name=data['name'], desc=data['desc'], price=data['price'])
        await message.reply(MSG['RUS']['STATES']['DATA_BASE'], parse_mode='markdown')
        await state.finish()
    else:
        await message.reply(MSG['RUS']['STATES']['MISTAKE']['INCORRECT INPUT'], parse_mode='Markdown')


# DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE
# @dp.message_handler(commands=['delsoft'])
async def delete_soft(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer(MSG['RUS']['ADMIN']['MSG_DELSOFT'], reply_markup=kb.get_softs_inlinekeyboard_4delete(), parse_mode='markdown')
    else:
        await message.reply(MSG['RUS']['STATES']['MISTAKE']['NO ROOTS'], parse_mode='markdown')


"""#################################  # # # # # # # # # # # # # ######################################"""
"""############################# # # # #       PARTNER       # # # # #################################"""
"""#################################  # # # # # # # # # # # # # ######################################"""

# ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD * ADD


# @dp.message_handler(commands=['addpartner'])
async def add_partner(message: types.Message):
    if message.from_user.id in admin_id:
        await PartnerStatesGroup.user_id.set()
        await message.answer(MSG['RUS']['STATES']['PARTNER']['ID'],
                             parse_mode='markdown',
                             reply_markup=kb.cancel_markup)
    else:
        await message.reply(MSG['RUS']['STATES']['MISTAKE']['NO ROOTS'], parse_mode='markdown')

# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.user_id)
async def load_userid(message: types.Message, state: FSMContext):
    if await cmd_state_cancel_admin(message, state):
        return
    if is_number(message.text):
        async with state.proxy() as data:
            data['user_id'] = message.text
        await PartnerStatesGroup.name.set()
        await message.reply(MSG['RUS']['STATES']['PARTNER']['NAME'], reply_markup=kb.cancel_markup, parse_mode='markdown')
    else:
        await message.reply(MSG['RUS']['STATES']['MISTAKE']['INCORRECT INPUT'], parse_mode='Markdown')

# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.name)
async def load_partnername(message: types.Message, state: FSMContext):
    if await cmd_state_cancel_admin(message, state):
        return
    async with state.proxy() as data:
        data['name'] = message.text
    await PartnerStatesGroup.promocode.set()
    await message.reply(MSG['RUS']['STATES']['PARTNER']['PROMO'], reply_markup=kb.cancel_markup, parse_mode='markdown')


# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.promocode)
async def load_promo(message: types.Message, state: FSMContext):
    if await cmd_state_cancel_admin(message, state):
        return
    async with state.proxy() as data:
        data['promocode'] = message.text
    await PartnerStatesGroup.discount.set()
    await message.reply(MSG['RUS']['STATES']['PARTNER']['DISCOUNT'], reply_markup=kb.cancel_markup, parse_mode='markdown')


# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.discount)
async def load_discount(message: types.Message, state: FSMContext):
    if await cmd_state_cancel_admin(message, state):
        return
    if is_number(message.text):
        async with state.proxy() as data:
            data['discount'] = message.text
        await PartnerStatesGroup.quantity.set()
        await message.reply(MSG['RUS']['STATES']['PARTNER']['QUANTITY'], reply_markup=kb.cancel_markup, parse_mode='markdown')
    else:
        await message.reply(MSG['RUS']['STATES']['MISTAKE']['INCORRECT INPUT'], parse_mode='Markdown')


# @dp.message_handler(lambda message: message.text, state=PartnerStatesGroup.quantity)
async def load_quantity(message: types.Message, state: FSMContext):
    if await cmd_state_cancel_admin(message, state):
        return
    if is_number(message.text):
        async with state.proxy() as data:
            data['quantity'] = message.text
        temporary_storage = data['user_id'], data['name'], data['promocode'], data['discount'], data['quantity']
        data_base.addpartner(data['user_id'], data['name'], data['promocode'], data['discount'], data['quantity'])
        await state.finish()
        await message.reply(MSG['RUS']['STATES']['DATA_BASE'], parse_mode='markdown')
    else:
        await message.reply(MSG['RUS']['STATES']['MISTAKE']['INCORRECT INPUT'], parse_mode='Markdown')


# DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE * DELETE

# @dp.message_handler(commands=['delpartner'], state=None)
async def delete_partner(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer(MSG['RUS']['ADMIN']['MSG_DELPARTNER'],
                             parse_mode = 'markdown',
                             reply_markup=kb.get_partners_inlinekeyboard_4delete())
    else:
        await message.reply(MSG['RUS']['STATES']['MISTAKE']['NO ROOTS'], parse_mode='markdown')


"""#################################  # # # # # # # # # # # # # ######################################"""
"""########################### # # # #       ADMIN HELP       # # # # ################################"""
"""#################################  # # # # # # # # # # # # # ######################################"""


# @dp.message_handler(commands=['admin_help'])
async def admin_help(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer(MSG['RUS']['ADMIN']['MSG_ADMIN_HELP'], parse_mode='markdown')
    else:
        await message.reply(MSG['RUS']['STATES']['MISTAKE']['NO ROOTS'], parse_mode='markdown')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(add_soft, commands=['addsoft'])
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



