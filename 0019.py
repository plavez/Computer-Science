
def is_anagram(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return s1, s2
    # if sorted(s1) == sorted(s2):
    #     return True
    # else:
    #     return False


result = is_anagram('Vlad islav', 'valsidalV')
print(result)
