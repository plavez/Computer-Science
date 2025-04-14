from numpy import stack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is None:
            raise IndexError('pop from empty stack')
        poppednode = self.head
        self.head = self.head.next
        return poppednode.data


a_stack = Stack()

a_stack.push(1)
a_stack.push(2)
a_stack.push(3)
a_stack.push(4)
a_stack.push(5)

for i in range(5):

    print(a_stack.pop())
