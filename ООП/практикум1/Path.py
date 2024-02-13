class Station:
    def __init__(self,paths=[],trains=[],workers=[]):
        self.paths = paths
        self.trains = trains
        self.workers = workers

    def add_path(self, path):
        self.paths.append(path)

    def add_train(self, train):
        self.trains.append(train)

    def add_worker(self, worker):
        self.workers.append(worker)

    def print_paths(self):
        for path in self.paths:
            print(path)

    def print_trains(self):
        for train in self.trains:
            print(train)

    def print_workers(self):
        for worker in self.workers:
            print(worker)

    def remove_path(self, path):
        self.paths.remove(path)

    def remove_train(self, train):
        self.trains.remove(train)

    def remove_worker(self, worker):
        self.workers.remove(worker)


station1 = Station()

station1.add_path('path1')
station1.add_path('path2')
station1.add_train('train1')
station1.add_worker('worker1')

station1.remove_path('path1')

station1.print_paths()
station1.print_trains()
station1.print_workers()


station2 = Station()

station2.add_path('path1')
station2.add_path('path2')
station2.add_train('train1')
station2.add_worker('worker1')

station2.remove_path('path1')

station2.print_paths()
station2.print_trains()
station2.print_workers()