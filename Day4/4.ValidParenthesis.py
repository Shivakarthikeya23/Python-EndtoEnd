def is_valid_parentheses(s):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pair[char]:
                return False
            stack.pop()

    return not stack


# Test
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("([)]"))  # False
print(is_valid_parentheses("{[]}"))  # True
