# Создатькласс  Vagon,  который  контролирует  создание объектов с именами, начинающимися с "vagon_".
# Метод __new__ проверяет, начинается ли имя с "vagon_", и если да, то удаляет "vagon_" из имени и устанавливает номер вагона.
# Затем он создает новый объект, добавляет его в словарь numbers и возвращает его.
# Метод __init__ не используется в данном классе, должен быть прописан пустым.

class Vagon:
    numbers = {}

    def __new__(cls, name, number):
        if not name.startswith("vagon_"):
            raise ValueError("Имя должно начинаться с 'vagon_'")
        name = name[6:]
        cls.numbers[name] = number
        return super().__new__(cls)

    def __init__(self, name, number):
        pass


v1 = Vagon("vagon_1", 1)
print(Vagon.numbers)  

