def solution(N, stages):
    total_user = [0]*(N+2)
    reach_user = [0]*(N+2)
    failure = {}
    
    for stage in stages:
        reach_user[stage] += 1
        for i in range(1, stage+1):
            total_user[i] += 1
    
    # print(reach_user)
    # print(total_user)
    
    for i in range(1, N+1):
        if total_user[i] != 0:
            failure[i] = reach_user[i]/total_user[i]
        else:
            failure[i] = 0
        
    # print(failure)
    
    answer = sorted(failure, key=lambda x: failure[x], reverse=True)
    
    
    return answer