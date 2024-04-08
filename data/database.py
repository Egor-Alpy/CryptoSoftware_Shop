import sqlite3 as sq
# указывать тип принимаемых переменных в функции

def edit_database(request, db_name="db_atshop.db"):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(request)

class DataBase():
    db_name = "db_atshop.db"
    def CREATE_DATABASE(self, db_name="db_atshop.db"):
        # создание БД
        with sq.connect(db_name) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users (
                indexx INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                name TEXT,
                refer_id TEXT
                )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS software (
                indexx INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price REAL
                )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS partners (
                indexx INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                name TEXT,
                promocode INTEGER,
                discount INTEGER,
                quantity INTEGER
                )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS purchases (
                            indexx INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            username TEXT,
                            user_github TEXT,
                            soft_name TEXT,
                            soft_price INTEGER,
                            refer_id INTEGER,
                            refer_discount INTEGER,
                            promocode INTEGER,
                            discount INTEGER,
                            total_discount INTEGER,
                            purchased INTEGER
                            )""")
    def __init__(self):
        pass
    def addpurchase(self, user_id, username, user_github, soft_name, soft_price, refer_id, refer_discount, promocode, discount, total_discount, purchased):
        edit_database(f"INSERT INTO purchases ('user_id', 'username', 'user_github', 'soft_name', 'soft_price', 'refer_id', 'refer_discount', 'promocode', 'discount', 'total_discount', 'purchased') VALUES ('{user_id}', '{username}', '{user_github}', '{soft_name}', '{soft_price}', '{refer_id}', '{refer_discount}', '{promocode}', '{discount}', '{total_discount}', '{purchased}')")
    def adduser(self, user_id, name, message):
        edit_database(f"INSERT INTO users('user_id', 'name', 'refer_id') VALUES({user_id}, '{name}', '{message.text[7::]}')")

    def addsoft(self, name, desc, price):
        edit_database(f"INSERT INTO software('name', 'description', 'price') VALUES('{name}', '{desc}', '{price}')")

    def delsoft(self, name):
        edit_database(f"DELETE FROM software WHERE name = '{name}'")

    def addpartner(self, user_id, name, promocode, discount, quantity):
        edit_database(f"INSERT INTO partners('user_id', 'name', 'promocode', 'discount', 'quantity') VALUES('{user_id}', '{name}', '{promocode}', '{discount}', '{quantity}')")

    def delpartner(self, user_id):
        edit_database(f"DELETE FROM partners WHERE user_id = '{user_id}'")

    def select_software_info(self, name):
        with sq.connect("db_atshop.db") as con:
            cur = con.cursor()
            cur.execute(f"SELECT name, description, price FROM software WHERE name = '{name}'")
            rows = cur.fetchall()
            return rows
