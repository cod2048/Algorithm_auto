from collections import deque

def solution(progresses, speeds):
    answer = []
    qProgressess = deque(progresses)
    qSpeeds = deque(speeds)
    days = 0
    cnt = 0
    
    while True:
        if not qProgressess:
            break
        if (qProgressess[0] + days*qSpeeds[0]) >= 100:
            qProgressess.popleft()
            qSpeeds.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            days += 1
            
    answer.append(cnt)
        
    return answer