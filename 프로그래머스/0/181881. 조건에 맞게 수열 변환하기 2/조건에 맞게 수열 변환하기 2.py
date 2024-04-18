import copy
def solution(arr):
    answer = 0
    arr1 = copy.deepcopy(arr)
    arr2 = copy.deepcopy(arr)
    
    for i, k in enumerate(arr1):
        if k >= 50 and k % 2 == 0:
            arr1[i] = int(k / 2)
        elif k < 50 and k % 2 == 1:
            arr1[i] = int(k * 2 + 1)
            
    while arr1 != arr2:
        for i, k in enumerate(arr1):
            if k >= 50 and k % 2 == 0:
                arr1[i] = int(k / 2)
            elif k < 50 and k % 2 == 1:
                arr1[i] = int(k * 2 + 1)
                
        for i, k in enumerate(arr2):
            if k >= 50 and k % 2 == 0:
                arr2[i] = int(k / 2)
            elif k < 50 and k % 2 == 1:
                arr2[i] = int(k * 2 + 1)
                
        answer += 1
        
    return answer