def solution(n, m):
    min_num = min(n, m)
    max_num = max(n, m)
    gcd = 0
    
    for num in range(1, min_num + 1):
        if min_num % num == 0 and max_num % num == 0:
            gcd = num
    
    lcm = n*m // gcd
    
    answer = [gcd, lcm]
    
    return answer