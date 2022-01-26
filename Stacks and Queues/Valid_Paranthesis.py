def isValid(s):

    stack = ['N']
    m = {')': '(', ']': '[', '}': '{'}
    for i in s:
            # If its a closed, check with the stack.pop element
            if i in m.keys():
                if stack.pop() != m[i]:
                    print('f')
                    return False
            # Append the open paranthesis to the stack        
            else:
                stack.append(i)
    print('t')
    return len(stack) == 1


s = '{[]}'
isValid(s)
