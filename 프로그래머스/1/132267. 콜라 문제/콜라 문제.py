def solution(a, b, n):
    answer = 0
    while n >= a:
        cokes = (n // a) * b
        n = (n % a) + cokes
        answer += cokes
    return answer