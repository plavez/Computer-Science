def binary_search(a_list, n):
    first = 0
    last = len(a_list)-1
    while last >= first:
        mid = (first+last)//2
        if a_list[mid] == n:

            return True
        else:
            if n < a_list[mid]:
                last = mid-1
            else:
                first = mid+1
    return False


print(binary_search([2, 3, 4, 5, 6, 25, 28, 38, 45], 3))
