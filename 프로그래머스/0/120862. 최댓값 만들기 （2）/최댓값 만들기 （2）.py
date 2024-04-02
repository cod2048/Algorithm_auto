def solution(numbers):
    numbers.sort()
    max_num = numbers[-1] * numbers[-2]
    min_num = numbers[0] * numbers[1]
    if max_num > min_num:
        answer = max_num
    else:
        answer = min_num
    return answer