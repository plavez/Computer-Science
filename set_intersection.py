# def return_intersection_set(set1, set2):
#     return list(set1 - set2)


# print(return_intersection({1, 1, 6, 8, 9, 4, }, {5, 9, 15, 25, 65}))


def return_intersection_list(set1, set2):
    return list(set1 & set2)


list11 = [11, 1, 1, 6, 8, 9, 4]
list22 = [11, 1, 1, 6, 8, 9, 4]
set1 = set(list11)
set2 = set(list22)
print(return_intersection_list(set1, set2))
