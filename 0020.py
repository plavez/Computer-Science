def is_palidrome(s1):
    if s1.lower() == s1[::-1].lower():
        return True
    return False


print(is_palidrome('WowW'))

s2 = 'Vlad'
print(s2[::1])
