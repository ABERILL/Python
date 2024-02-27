# Написать  программу,  которая  создает  класс  DataBaseс методами  для  работы  с  базой  данных.
# Программа  должна  принимать параметры пользователя, пароль и порт при создании экземпляра класса и
# вывыводить сообщение о подключении к базе данных при вызове метода connect.
# Используя метод __new__ реализовать возможность создания только одного объекта  соединения DataBase.
# Доказать,  что  создать  несколько  объектов соединения к одной базе данных нельзя. В памяти может быть только один объект класса  DataBase.

class DataBase():
    _instanse = None

    def __new__(cls, *args, **kwargs):
        if cls._instanse is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,user,psw,port):
        self.user = user
        self.psw = psw
        self.port = port
    
    def __str__(self):
        return f"Подключение к БД: {self.user}, {self.psw}, {self.port}"

    def connect(self):
        print(f"Подключение к БД: {self.user}, {self.psw}, {self.port}")

    def __del__(self):
        print("Закрытие соединения с БД")

    def get_data(self):
        print("Получение данных из БД")

    def set_data(self):
        print("Запись данных в БД")

# Создание одного объекта
db_instance = DataBase(user="root", psw="1234", port=80)
db_instance.connect()

# Попытка создания второго объекта (не удастся)
second_db_instance = DataBase(user="user", psw="pass", port=8080)

# Демонстрация методов работы с данными
db_instance.get_data()
db_instance.set_data()

# Удаление объекта (закрытие соединения)
del db_instance

