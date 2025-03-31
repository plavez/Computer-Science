# import time

# start = time.time()
# for i in range(1, 6):
#     print(i)

# end = time.time()
# print(f"{end-start} seconds")

from itertools import count


def print_it(n):
    count = 0
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)
        for j in range(n):
            print(j)
            count += 1
            print(count)
            for h in range(n):
                print(h)
                # count += 1
                # print(count)


print_it(10)
