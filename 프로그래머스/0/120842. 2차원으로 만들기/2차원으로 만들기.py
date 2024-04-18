def solution(num_list, n):
    answer = []
    i = 0
    
    while i < len(num_list):
        tmp = []
        for j in range(i, len(num_list)):
            if len(tmp) == n:
                answer.append(tmp)
                break
            tmp.append(num_list[j])
            i += 1
   
    if tmp:
        answer.append(tmp)
            
    return answer