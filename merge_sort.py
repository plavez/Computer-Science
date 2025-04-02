# def merge_sort(a_list):
#     if len(a_list) > 1:
#         mid = len(a_list)//2
#         left_half = a_list[:mid]
#         right_half = a_list[mid:]
#         merge_sort(left_half)
#         merge_sort(right_half)

#         left_ind = 0
#         right_ind = 0
#         alist_ind = 0
#         while left_ind < len(left_half) and right_ind < len(right_half):
#             if left_half[left_ind] <= right_half[right_ind]:
#                 a_list[alist_ind] = left_half[left_ind]
#                 left_ind += 1
#             else:
#                 a_list[alist_ind] = right_half[right_ind]
#                 right_ind += 1
#             alist_ind += 1

#         while left_ind < len(left_half):
#             a_list[alist_ind] = left_half[left_ind]
#             left_ind += 1
#             alist_ind += 1

#         while right_ind < len(right_half):
#             a_list[alist_ind] = right_half[right_ind]
#             right_ind += 1
#             alist_ind += 1


# print(merge_sort([6, 3, 9, 2]))
def merge_sort(a_list, depth=0):
    indent = "  " * depth  # отступ для визуализации уровня рекурсии
    print(f"{indent}Разделяем: {a_list}")

    if len(a_list) > 1:
        mid = len(a_list)//2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half, depth + 1)
        merge_sort(right_half, depth + 1)

        left_ind = 0
        right_ind = 0
        alist_ind = 0

        print(f"{indent}Сливаем: {left_half} и {right_half}")

        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                print(
                    f"{indent}  Берём {left_half[left_ind]} из левой половины")
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                print(
                    f"{indent}  Берём {right_half[right_ind]} из правой половины")
                right_ind += 1
            alist_ind += 1

        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            print(
                f"{indent}  Копируем оставшийся {left_half[left_ind]} из левой")
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind] = right_half[right_ind]
            print(
                f"{indent}  Копируем оставшийся {right_half[right_ind]} из правой")
            right_ind += 1
            alist_ind += 1

        print(f"{indent}После слияния: {a_list}")


print(merge_sort([6, 3, 9, 2]))
