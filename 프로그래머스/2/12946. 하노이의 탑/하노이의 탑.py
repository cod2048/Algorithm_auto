def hanoi(num, start, end, answer):
    if num == 1:
        answer.append([start, end])
        return
    hanoi(num-1, start, 6-start-end, answer)
    answer.append([start, end])
    hanoi(num-1, 6-start-end, end, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, answer)
    return answer
