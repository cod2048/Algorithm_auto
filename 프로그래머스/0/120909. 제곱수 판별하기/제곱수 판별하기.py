def solution(n):
    answer = 2
    for i in range(1, int(n**0.5)+1):
        if i**2 == n:
            answer = 1
            break
    return answer