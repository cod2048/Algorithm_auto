from collections import deque

def is_balanced(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def separate(brackets):
    count_left = 0
    count_right = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            count_left += 1
        elif brackets[i] == ')':
            count_right += 1
        if count_left == count_right:
            return brackets[:i+1], brackets[i+1:]  

def solution(brackets):
    if(brackets == ''):
        return ''
    
    answer = ''
    u, v = separate(brackets)
    if is_balanced(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for c in u[1:-1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('
        return answer
        