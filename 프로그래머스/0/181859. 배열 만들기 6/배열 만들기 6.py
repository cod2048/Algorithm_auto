def solution(arr):
    answer = []
    i = 0
    
    while len(arr) > i:
        if not answer:
            answer.append(arr[i])
        else:
            if answer[-1] == arr[i]:
                answer.pop()
            else:
                answer.append(arr[i])
        i += 1
    
    if not answer:
        answer.append(-1)
        
    return answer