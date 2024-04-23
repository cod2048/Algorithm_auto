from collections import defaultdict

def solution(array):
    answer = 0
    array_dic = defaultdict(int)
    
    for num in array:
        array_dic[num] += 1
    
    answer = sorted(array_dic.items(), key = lambda x: x[1], reverse = True)
    
    if len(answer) > 1 and answer[0][1] == answer[1][1]:
        return -1
    
    return answer[0][0]