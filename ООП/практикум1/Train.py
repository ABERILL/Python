class Train:
    def __init__(self,wagons = [], cargo = []):
        self.wagons = wagons
        self.cargo = cargo

    def append_wagon(self, wagon,cargo):
        self.wagons.append(wagon)
        self.cargo.append(cargo)
    
    def remove_wagon(self, wagon,cargo):
        self.wagons.remove(wagon)
        self.cargo.remove(cargo)

    def print_wagons(self):
        for wagon in self.wagons:
            print(wagon)
    
    def print_cargo(self):
        for cargo in self.cargo:
            print(cargo) 

train1 = Train()
train1.append_wagon('вагон1',30)
train1.append_wagon('вагон2',10)
train1.append_wagon('вагон3',20)
train1.remove_wagon('вагон1',30)
train1.print_wagons()
train1.print_cargo()


train2 = Train()
train2.append_wagon('вагон10', 33)
train2.append_wagon('вагон20', 13)
train2.append_wagon('вагон30', 23)
train2.remove_wagon('вагон10', 33)
train2.print_wagons()
train2.print_cargo()
