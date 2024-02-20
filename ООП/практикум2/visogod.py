class Visogod:
    def __init__(self,god):
        self.god = god

    def is_year_leap(self,god):
        if (self.god % 4==0 and self.god %100 !=0) or (self.god %400 == 0):
            return True
        else:
            return False

# Создаем экземпляр класса с годом 1999
abc = Visogod(1999)

# Цикл, который повторяется 100 раз
for god in range(2000, 2100):
    obj = Visogod(god)
    print(god, obj.is_year_leap(god))
