def solution(rank, attendance):
    result = []
    answer = 0
    for i in range(len(attendance)):
        if attendance[i]:
            result.append([rank[i], i])
    
    result.sort(key = lambda x : x[0])
    
    answer = result[0][1] * 10000 + result[1][1] * 100 + result[2][1]    
    return answer