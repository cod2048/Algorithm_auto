def solution(a, b):
    answer = 0
    if a % 2 == 1 and b % 2 == 1:
        answer = a*a + b*b
    else:
        answer = abs(a-b)
    if (a+b) % 2 == 1:
        answer = 2*(a+b)
    return answer