# def two_sum(a_list, target):
#     a_dict = {}
#     for index, n in enumerate(a_list):
#         rem = target - n
#         if rem in a_dict:
#             return index, a_dict[rem]
#         else:
#             a_dict[n] = index


# print(two_sum((-1, 2, 3, 4, 7), 5))


def search_and_remove(a_string):
    a_list = []
    a_list = a_string.split()
    a_dict = {}
    for index, value in enumerate(a_list):
        return index, value


print(search_and_remove(
    "I am a self-taught programmer looking for a job as a programmer."))
