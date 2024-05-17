def solution(n):
    answer = 0
    formation_3 = ""
    i = 1
    
    while n > 0:
        formation_3 += str(n % 3)
        n = n // 3
    
    for j in range(len(formation_3)-1, -1 ,-1):
        answer += i * int(formation_3[j])
        i *= 3
        
    
    return answer