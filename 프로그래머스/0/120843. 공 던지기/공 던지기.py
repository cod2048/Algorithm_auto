def solution(numbers, k):
    answer = 0
    tmp = numbers * k
    answer = tmp[2*(k-1)]
    
    return answer