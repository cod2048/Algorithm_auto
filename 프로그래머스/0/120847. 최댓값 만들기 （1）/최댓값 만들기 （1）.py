def solution(numbers):
    numbers.sort()
    answer = numbers.pop() * numbers.pop()
    return answer