class Worker:
    def __init__(self, id, info_radio, name, post, trains=[]):
        self.id = id
        self.info_radio = info_radio
        self.name = name
        self.post = post
        self.trains = trains


worker1 = Worker(1, 'radio1', 'Иван Иванов', 'Мастер', ['поезд1', 'поезд2'])
print(worker1.id)
print(worker1.info_radio)
print(worker1.trains)
print(worker1.name)
print(worker1.post)

worker2 = Worker(2, 'radio1', 'Иван Rusakov', 'Ingener', ['поезд10', 'поезд20'])
print(worker2.id)
print(worker2.info_radio)
print(worker2.trains)
print(worker2.name)
print(worker2.post)
