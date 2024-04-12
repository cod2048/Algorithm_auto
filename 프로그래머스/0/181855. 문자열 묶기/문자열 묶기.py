def solution(strArr):
    answer = 0
    len_arr = [0 for i in range(len(strArr))]
    for i in strArr:
        len_arr[len(i)] += 1
    
    answer = max(len_arr)
    return answer