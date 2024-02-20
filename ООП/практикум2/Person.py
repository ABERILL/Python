from datetime import date
class Person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth = date_of_birth

    def calculate_age(self,current_time=date(2024,2,24)):
        age = current_time.year - self.date_of_birth.year
        if current_time.month < self.date_of_birth.month or (current_time.month == self.date_of_birth.month and current_time.day < self.date_of_birth.day):
            age -= 1
        return age


person1 = Person("Иванов Иван Иванович", "Россия", date(1946, 8, 15))
person2 = Person("Петров Сергей Александрович", "Белоруссия", date(1982, 10, 22))
person3 = Person("Федоров Андрей Алексеевич", "Китай", date(2020, 2, 1))

print("Персона 1:")
print("Имя: ", person1.name)
print("Страна: ", person1.country)
print("Дата рождения: ", person1.date_of_birth)
print("Возраст: ", person1.calculate_age())

print("Персона 2:")
print("Имя: ", person2.name)
print("Страна: ", person2.country)
print("Дата рождения: ", person2.date_of_birth)
print("Возраст: ", person2.calculate_age())
