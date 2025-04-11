def return_inner(list1, list2):
    list3 = [same_number for same_number in list1 if same_number in list2]
    return list3


list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
print(return_inner(list1, list2))
