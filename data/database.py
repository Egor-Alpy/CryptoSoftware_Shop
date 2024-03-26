import sqlite3 as sq
# указывать тип принимаемых переменных в функции

class DataBase():
    @staticmethod
    def edit_database(request):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(request)

    def __init__(self):
        pass

    def adduser(self, user_id, name, message):
        edit_database(f"INSERT INTO users VALUES({user_id}, '{name}', '{message.text[7::]}')")

    def addsoft(self, name, desc, price):
        edit_database(f"INSERT INTO software VALUES('{name}', '{desc}', '{price}')")

    def delsoft(self, name):
        edit_database(f"DELETE FROM software WHERE name = '{name}'")

    def addpartner(self, user_id, name, promocode, discount, quantity):
        edit_database(f"INSERT INTO partners VALUES('{user_id}', '{name}', '{promocode}', '{discount}', '{quantity}')")

    def delpartner(self, user_id):
        edit_database(f"DELETE FROM partners WHERE user_id = '{user_id}'")

    def select_software_info(self, name):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(f"SELECT name, description, price FROM software WHERE name = '{name}'")
            rows = cur.fetchall()
            return rows
