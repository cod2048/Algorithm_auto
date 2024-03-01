def solution(participant, completion):
    dic = {}
    
    for person in participant:
        if person in dic:
            dic[person] += 1
        else:
            dic[person] = 1

    for person in completion:
        if dic[person] == 1:
            del dic[person]
        else:
            dic[person] -= 1
    
    answer = list(dic.keys())[0]
    
    return answer