def solution(n):
    answer = []
    divide_num = 2
    while divide_num <= n:
        if n % divide_num == 0:
            answer.append(divide_num)
            n = n / divide_num
        else:
            divide_num += 1
    return list(dict.fromkeys(answer))