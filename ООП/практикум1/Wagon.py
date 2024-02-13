class Wagon:
    def __init__(self,numbers_trains = [],wagons = []):
        self.numbers_trains = numbers_trains
        self.wagons = wagons
    
    def append_number_train(self,number_train):
        self.numbers_trains.append(number_train)

    def remove_number_train(self,number_train):
        self.numbers_trains.remove(number_train)

    def get_number_train(self,wagon):
        return self.numbers_trains


    