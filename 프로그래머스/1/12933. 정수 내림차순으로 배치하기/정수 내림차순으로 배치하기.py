def solution(n):
    answer = []
    
    for number in str(n):
        answer.append(number)
        
    answer.sort(reverse = True)
    
    return int(''.join(answer))