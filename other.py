from data.TEXT import *
from foundation.admin import *

# Проверка: является ли сообщение числом
def is_number(msg):
    try:
        float(msg)
        return True
    except:
        return False

# Остановка машины состояния при вызове новой команды и вызов этой команды
async def cmd_state_cancel(message, state):
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


async def get_menu(message, message_id):
    pass

