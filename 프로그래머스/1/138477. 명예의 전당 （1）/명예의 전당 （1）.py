def solution(k, score):
    answer = []
    hall = []
    
    for s in score:
        if len(hall) < k:
            hall.append(s)
        else:
            if s > min(hall):
                hall.remove(min(hall))
                hall.append(s)
        
        answer.append(min(hall))
    
    return answer