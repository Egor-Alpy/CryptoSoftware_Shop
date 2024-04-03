# ========================================    IMPORT    ===============================================
from aiogram import Bot, Dispatcher

from config import token
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import database as db


# Экземпляр класса БД
data_base = db.DataBase()

# Создание Базы Данных
data_base.CREATE_DATABASE()

# Временное хранилище
storage = MemoryStorage()

# инициализация бота
bot = Bot(token)
dp = Dispatcher(bot=bot,
                storage=storage)
