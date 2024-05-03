def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        tmp = 1
        
        for i in range(1, num):
            if num % i == 0:
                tmp += 1
                
        if tmp % 2 == 0:
            answer += num
        else:
            answer -= num
            
    return answer