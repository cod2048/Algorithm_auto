def solution(array, n):
    answer = 0
    array.append(n)
    array.sort()
    target = array.index(n)
    
    if target == len(array) - 1:
        return array[-2]
    
    if target == 0:
        return array[1]
    
    answer = (target - 1) if abs(n - array[target - 1]) <= abs(n - array[target + 1]) else (target + 1)
    
    return array[answer]