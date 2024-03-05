def solution(want, number, discount):
    dic = {}
    answer = 0
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    j = 0
    while True:
        if (j + 10) > len(discount):
            break
            
        target_days = discount[j:j+10]
        dic_copy = dic.copy()

        for item in target_days:
            if item in dic_copy and dic_copy[item] > 0:
                dic_copy[item] -= 1
        
        if all(value == 0 for value in dic_copy.values()):
            answer += 1
        j += 1
        
    return answer