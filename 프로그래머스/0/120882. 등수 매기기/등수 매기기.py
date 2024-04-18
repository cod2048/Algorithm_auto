def solution(score):
    answer = []
    average = []
    result = []
    for eng, math in score:
        average.append((eng + math) / 2)
        result.append((eng + math) / 2)
        
    average.sort(reverse = True)
    
    for i in result:
        answer.append(average.index(i) + 1)
        
        
    return answer