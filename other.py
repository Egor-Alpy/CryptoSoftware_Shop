# Проверка: является ли сообщение числом
def is_number(msg):
    try:
        float(msg)
        return True
    except:
        return False
