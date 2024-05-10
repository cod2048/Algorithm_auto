def solution(s):
    stack = []
    
    for letter in s:
        if len(stack) != 0 and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
        
    if stack:
        return 0
    else:
        return 1