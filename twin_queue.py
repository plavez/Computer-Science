class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(item)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Cannon pop from empty queue")
        return self.s1.pop()


numbers = Queue()
numbers.enqueue(1)
print(numbers.dequeue())
numbers.enqueue(2)
print(numbers.dequeue())
