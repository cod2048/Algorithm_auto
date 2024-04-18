from collections import deque

def solution(A, B):
    answer = 0
    
    if A == B:
        return 0
    
    A = deque(A)
    B = deque(B)
    
    for _ in range(len(A)):
        if A == B:
            break
        A.appendleft(A.pop())
        answer += 1
    else:
        answer = -1
    
    return answer