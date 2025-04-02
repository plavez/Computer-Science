def buble_sort(a_list):
    list_lenght = len(a_list)-1
    for i in range(list_lenght):
        for j in range(list_lenght):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list


print(buble_sort([11, 55, 1, 8, 15, 2, 5]))
