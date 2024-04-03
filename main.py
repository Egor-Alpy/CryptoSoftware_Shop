# ========================================    IMPORT    ===============================================
from aiogram import Bot, types, executor, Dispatcher

import StatesGroups
from bot_creation import *
from foundation import *

async def on_startup(_):
    print('_____Bot is running_____')

StatesGroups.register_handlers_cancel_state(dp)
# callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
client.register_handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
