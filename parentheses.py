def check_parentheses(a_string):
    stack = []
    for c in a_string:
        if c == '(' or c == '{':
            stack.append(c)
        if c == ')' or c == '}':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0


print(check_parentheses('{}(){{()}'))
