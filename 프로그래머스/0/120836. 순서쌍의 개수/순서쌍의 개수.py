def solution(n):
    answer = 0
    start = 1
    end = n
    while end > 0 and start <= n:
        if start * end == n:
            answer += 1
            start += 1
            end -= 1
        elif start * end < n:
            start += 1
        else:
            end -= 1
            
    return answer