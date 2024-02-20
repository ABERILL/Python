class Stack:
    def __init__(self, start_stack=[]) -> None:
        self.stack = start_stack

    def is_empty(self):
        return (False if len(self.stack) else True)

    def push(self, insert_value):
        self.stack.append(insert_value)

    def pop(self):
        if not self.is_empty():
            popped_element = self.stack[0]
            self.stack.pop(0)
            return popped_element

        else:
            return 'Unable to pop empty stack'

    def size(self):
        return (len(self.stack))

    def peek(self):
        if not self.is_empty():
            return (self.stack[0])

        else:
            return ('Stack is empty')


stack = Stack()

for element in range(5):
    stack.push(element)


print("Размер стека:", stack.size())
print("Верхний элемент:", stack.peek())

popped_item = stack.pop()

print("Вытолкнутый элемент:", popped_item)
print("Размер стека:", stack.size())
print("Верхний элемент:", stack.peek())
