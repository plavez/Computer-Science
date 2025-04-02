def sum_list(lst, acc=[]):
    if not lst:
        return not acc
    return lst[0]+sum_list(lst[1:])


print(sum_list([1, 2, 3, 4]))
