# Создать  класс,  который  считает  количество  созданных объектов класса и может создать не более 5 объектов.
# При создании 6-го объекта появляется сообщение о превышении лимита созданных объектов

class LimitedInstances():

    _instances = []
    limit = 5

    def __new__(cls):
        if len(cls._instances) >= cls.limit:
            raise RuntimeError("Превышен лимит на количество объектов")

        instance = super().__new__(cls)
        cls._instances.append(instance)
        return instance

    def __del__(self):
        LimitedInstances._instances.remove(self)

object1 = LimitedInstances()
object2 = LimitedInstances()
object3 = LimitedInstances()
object4 = LimitedInstances()
object5 = LimitedInstances()
object6 = LimitedInstances()
