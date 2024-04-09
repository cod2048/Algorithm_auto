def solution(a, d, included):
    answer = 0
    numbers = [a]
    for i in range(len(included)):
        numbers.append(numbers[i] + d)
    for i in range(len(included)):
        if included[i]:
            answer += numbers[i]
    return answer