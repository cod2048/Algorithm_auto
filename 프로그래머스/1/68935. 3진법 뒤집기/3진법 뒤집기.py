def solution(n):
    answer = 0
    formation_3 = ""
    
    while n > 0:
        formation_3 += str(n % 3)
        n = n // 3
    
    answer = int(formation_3, 3)
    
    return answer