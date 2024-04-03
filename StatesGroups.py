from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


# Add soft state
class ClientStatesGroup(StatesGroup):
    name = State()
    desc = State()
    price = State()


# Add partner state
class PartnerStatesGroup(StatesGroup):
    user_id = State()
    name = State()
    promocode = State()
    discount = State()
    quantity = State()


# =====================================      CANCEL      =================================================

# @dp.message_handler(commands=['cancel'], state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('*Выполнена отмена*', parse_mode='markdown')
    await state.finish()


def register_handlers_cancel_state(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, commands=['cancel'], state="*")

