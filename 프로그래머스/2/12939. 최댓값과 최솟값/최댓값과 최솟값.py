def solution(s):
    answer = ''
    num_list = list((s.split()))
    int_list = []
    
    for num in num_list:
        int_list.append(int(num))
        
    min_num = min(int_list)
    max_num = max(int_list)
    
    answer += str(min_num)
    answer += " "
    answer += str(max_num)
        
    return answer