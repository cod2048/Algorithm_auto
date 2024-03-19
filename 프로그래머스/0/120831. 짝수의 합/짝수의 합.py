def solution(n):
    answer = 0
    sum_num = 2
    while sum_num <= n:
        answer += sum_num
        sum_num += 2
    return answer