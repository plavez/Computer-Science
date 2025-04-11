from collections import deque


# def linked_list(data):
#     a_list = deque()
#     for i in data:
#         a_list.append(i)
#     return a_list


# a_list = linked_list(['Harry', 'Potter'])
# # a_list = linked_list('Potter')
# print(a_list[1])
# print(type(a_list))


def linked_list_range():
    a_list = deque()
    for i in range(1, 11):
        a_list.append(i)
    return a_list


def linnked_list_2():
    a_list = []
    for i in range(1, 11):
        a_list.append(i)
    return a_list


a_list = linked_list_range()
print(a_list)
a_list.appendleft(222)
print(a_list)
a_list.popleft()
print(a_list)
a_list.reverse()
print(a_list)

b_list = linnked_list_2()
print(b_list)
b_list.reverse()
print(b_list)
