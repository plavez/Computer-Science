def gsf(i1, i2):
    gsf = None
    if i1 == 0:
        return i2
    if i2 == 0:
        return i1
    if i1 > i2:
        smaller = i2
    else:
        smaller = i1
    for i in range(1, smaller+1):
        if i1 % i == 0 and i2 % i == 0:
            gsf = i
    return gsf


print(gsf(0, 24))
