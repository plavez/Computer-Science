from bisect import bisect_left


def binary_search(an_itaribale, target):
    index = bisect_left(an_itaribale, target)
    if index <= len(an_itaribale) and an_itaribale[index] == target:
        return True
    return False


print(binary_search(sorted([10, 25, 2, 11, 13, 56, 12]), 'ff'))
