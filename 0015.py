def power_tail(a, n, acc=1):
    if n == 0:
        return acc
    return power_tail(a, n - 1, acc * a)


print(power_tail(2, 3))
