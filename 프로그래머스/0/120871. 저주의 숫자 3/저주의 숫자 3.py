def solution(n):
    answer = 0
    cnt = 0
    
    while cnt < n:
        answer += 1
        if "3" in str(answer) or answer % 3 == 0:
            continue
        cnt += 1
        
    
    return answer