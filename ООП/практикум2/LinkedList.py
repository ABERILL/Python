class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Пока есть элементы, после которых идет что-то еще, продолжаем цикл, после чего - в последний элемент пихаем новый экземпляр узла
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def delete(self, data):
        if self.head is None:
            return self.head

        if self.head.data == data:
            self.head = self.head.next
            return data

        current = self.head

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return data

            current = current.next


linked_list = LinkedList()

for element in range(5):
    linked_list.insert(element)

print("Исходный связанный список:")
linked_list.display()

linked_list.insert(5)
print("После вставки нового узла (5):")
linked_list.display()

linked_list.delete(2)
print("После удаления существующего узла (2):")
linked_list.display()
