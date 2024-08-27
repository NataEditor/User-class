class DataBase:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя содержащий атрибуты: логин, пароль.

    """

    def __int__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = DataBase()
    user = User(input("Введите логин "), password := input("Введите пароль "), password2 := input("повторите пароль "))
    if password != password2:
        exit()
    database.add_user(user.username, user.password)
