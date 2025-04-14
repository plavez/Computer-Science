def reverse_string(a_string):
    stack = []
    string = ''
    for c in a_string:
        stack.append(c)

    for c in range(len(a_string)):
        string += stack.pop()
    return string


print(reverse_string('Vladislav'))
