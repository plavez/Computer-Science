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
    a_list = a_string.split()
    seen = set()
    for index, value in enumerate(a_list):
        word = value.lower().strip(".,!?")
        if word in seen:
            return index, value
        seen.add(word)
    return None


print(search_and_remove(
    "I am a self-taught programmer looking for a job as a programmer."))


def search_and_remove_2(a_string):
    a_list = a_string.split()
    seen = set()

    for index, word in enumerate(a_list):
        cleaned = word
        if cleaned in seen:
            del a_list[index]
            return ' '.join(a_list)
        seen.add(cleaned)
    return a_string


print(search_and_remove_2(
    "I am a self-taught programmer looking for a job as a programmer."))
