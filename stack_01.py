class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_items(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


a_stack = Stack()
a_stack.push(4)
print(a_stack.pop())
print(a_stack.is_items())
a_stack.push(4)
a_stack.push(5)
a_stack.push(44)
a_stack.push(365.5)
a_stack.push(36)
print(a_stack.size())
print(a_stack.peek())
