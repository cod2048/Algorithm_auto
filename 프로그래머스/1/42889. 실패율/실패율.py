def solution(N, stages):
    total_user = [0]*(N+2)
    reach_user = [0]*(N+2)
    failure = {}
    
    for stage in stages:
        reach_user[stage] += 1
        # for i in range(1, stage+1):
        #     total_user[i] += 1
        
    total_user[N + 1] = reach_user[N + 1]
    for i in range(N, 0, -1):
        total_user[i] = total_user[i + 1] + reach_user[i]
    
    # print("reach_user" , reach_user)
    # print("total_user" , total_user)
    
    for i in range(1, N+1):
        if total_user[i] != 0:
            failure[i] = reach_user[i]/total_user[i]
        else:
            failure[i] = 0
        
    # print(failure)
    
    answer = sorted(failure, key=lambda x: failure[x], reverse=True)
    
    
    return answer
