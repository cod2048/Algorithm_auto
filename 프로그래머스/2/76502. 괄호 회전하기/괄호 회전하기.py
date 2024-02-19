def is_correct(buckets):
    stack = []
    for bucket in buckets:
        if bucket in ('(', '[', '{'):
            stack.append(bucket)
        else:
            if not stack:
                return False
            if bucket == ')' and stack[-1] == '(':
                stack.pop()
            if bucket == '}' and stack[-1] == '{':
                stack.pop()
            if bucket == ']' and stack[-1] == '[':
                stack.pop()
    
    return len(stack) == 0
    

def solution(s):
    answer = 0
    for _ in range(len(s)):
        if is_correct(s):
            answer += 1
        s = s[1:] + s[:1]
    
    return answer