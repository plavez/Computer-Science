class MinStack:
    def __init__(self):
        self.main = []
        self.min = []

    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)

        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]


tracking_stack = MinStack()
# a_stack = ['Vladislav', 'Marina', 'Emma',
#    'Vadim', 'Asia', 'Arisha', 'Papa', 'Mama', 'Aaaa','Bbbb']
# for i in a_stack:
#     tracking_stack.push(i)
tracking_stack.push(10)
# print(tracking_stack.get_min())
# print(tracking_stack.pop())
print(tracking_stack.main)
print(tracking_stack.min)
