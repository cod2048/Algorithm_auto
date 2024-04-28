def solution(n):
    answer = -1
    
    for num in range(1, n // 2 + 2):
        if num * num == n:
            answer = (num + 1) * (num + 1)
            break
            
    return answer