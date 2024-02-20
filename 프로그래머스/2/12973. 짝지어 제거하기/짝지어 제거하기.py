def solution(s):
    stack = []
    
    for x in s:
        if len(stack) != 0 and stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
        
    if stack:
        return 0
    else:
        return 1