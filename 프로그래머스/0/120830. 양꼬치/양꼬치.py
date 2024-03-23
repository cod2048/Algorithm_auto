def solution(n, k):
    answer = 0
    food = n * 12000
    drink = k * 2000
    free_drink = n // 10 * 2000
    answer = food + drink - free_drink
    return answer