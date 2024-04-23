def solution(a, b):
    min_num = min(a, b)
    max_num = max(a, b)
    gcd = 0
    for i in range(1, min_num + 1):
        if (min_num % i == 0) and (max_num % i == 0):
            gcd = i
    b = b // gcd
    
    while True:
        if b % 5 != 0:
            break
        b = b // 5
    
    while True:
        if b % 2 != 0:
            break
        b = b // 2
    
    if b == 1:
        return 1
    
    return 2