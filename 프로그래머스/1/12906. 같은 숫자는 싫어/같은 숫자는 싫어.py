def solution(arr):
    tmp = arr[0]
    answer = [tmp]
    
    for num in arr:
        if num != tmp:
            answer.append(num)
            tmp = num
        
    return answer