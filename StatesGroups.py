from aiogram.dispatcher.filters.state import StatesGroup, State
class ClientStatesGroup(StatesGroup):
    name = State()
    desc = State()
    price = State()

class PartnerStatesGroup(StatesGroup):
    user_id = State()
    name = State()
    promocode = State()
    discount = State()
    quantity = State()


