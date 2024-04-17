def solution(emergency):
    answer = []
    priority = sorted(emergency, reverse = True)
    for patient in emergency:
        answer.append(priority.index(patient)+1)
    
    return answer