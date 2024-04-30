def solution(arr, divisor):
    answer = []
    
    for number in arr:
        if number % divisor == 0:
            answer.append(number)
            
    answer.sort()
    
    if not answer:
        answer.append(-1)
    
    return answer