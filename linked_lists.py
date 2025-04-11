from platform import node
import random
from collections import deque


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def linked_list(self, data_for_list):
        self.data_for_list = deque()
        self.data_for_list.append(data_for_list)

    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        raise IndexError("Index out of range")

    # def __str__(self):
    #     result = []
    #     node = self.head
    #     while node is not None:
    #         result.append(str(node.data))
    #         node = node.next
    #     return " ----> ".join(result)

    def remove(self, target):
        if self.head == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
            self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False


a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
a_list.append('Monday')
a_list.append("Wednesday")
a_list.append("Tuesday")
b_list = LinkedList()
b_list.linked_list(b_list.)
print(b_list)
print(a_list.__str__())
