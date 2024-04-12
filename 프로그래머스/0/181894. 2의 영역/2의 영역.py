def solution(arr):
    answer = [-1]
    start = 0
    end = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] == 2:
            break
        start += 1
    
    
    for j in range(len(arr)-1, -1, -1):
        if arr[j] == 2:
            break
        end -= 1
    
    if start == len(arr) and end == -1:
        return answer
    
    else:
        answer.pop()
        answer = arr[start:end + 1]
    
    return answer