def return_inner(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))


list1 = [2, 43, 48, 62, 64, 28, 3, 31, 4, 70, 14]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
new_list = return_inner(list1, list2)
print(type(new_list))
print(new_list)


def return_inner_for3(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    return list(set1.intersection(set2, set3))


list1 = [2, 43, 48, 62, 64, 28, 3, 31, 33, 4, 656, 70, 14, 1]
list2 = [1, 28, 42, 70, 2, 656, 10, 62, 31, 4, 14, 1]
list3 = [1, 28, 42, 77, 2, 10, 62, 33, 4, 14, 656, 1]
new_list2 = return_inner_for3(list1, list2, list3)
print(type(new_list2))
print(new_list2)
