def sum_numbers(n):
    if n < 10:
        return n
    return (n % 10)+sum_numbers(n//10)


print(sum_numbers(11))
