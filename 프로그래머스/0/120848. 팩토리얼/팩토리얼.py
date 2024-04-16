def solution(n):
    answer = 0
    result = 1
    number = 1
    
    while True:
        if result > n:
            break
        number += 1
        result *= number
    
    return number-1