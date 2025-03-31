pin = 934556789
n = len(str(pin))
print(n)
for i in range(10**n):
    if i == pin:
        print(i)
