def numbers(n):
    if n > 10:
        return
    print(n)
    numbers(n+1)


numbers(1)
