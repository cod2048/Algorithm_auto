def solution(n):
    answer = 6
    while True:
        if answer % n == 0:
            break
        answer += 6
    return answer / 6