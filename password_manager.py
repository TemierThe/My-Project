from cryptography.fernet import Fernet

#   ключ + пароль + текст для шифрования = случайный текст
#   случайный текст + ключ + пароль = текст для шифрования

'''
#   генерация ключа
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


# определяем функцию просмотра
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())    # убираем перенос строки

            # создаем 2 переменные и помещаем в них данные из файла, полученные при разделении (.split())
            user, passw = data.split("|", 1)
            print ("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

# определяем функцию добавления
def add():
    name = input ('Имя аккаунта: ')
    pwd = input ("Пароль: ")

# 'w' - открывает файл для записи (если файла нет, может перезаписать и удалить всю инфо), 'r' - режим чтения, 'a' - режим добавления
# файл может быть открыт в двоичном 'ab' или текстовом режиме 'at' (по умолчанию, если не указано)
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input ("Хотите ли Вы добавить новый пароль или просмотреть существующие (просмотр, добавление), нажмите Q чтобы выйти? ").lower()
    if mode == "q":
        break
    if mode == "просмотр":
        view()    # вызов ф. просмотра
    elif mode == "добавление":
        add()    # вызов ф. добавления
    else:
        print ("Некорректное значение")
    continue