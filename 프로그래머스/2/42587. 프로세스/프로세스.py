from collections import deque

def solution(priorities, location):
    answer = 0
    process = 65
    process_priorities = deque()
    
    # 프로세스의 이름을 A부터 순차적으로 부여하고 우선순위와 함께 저장
    for i in range(len(priorities)):
        process_priorities.append((priorities[i], chr(process)))
        process += 1
        
    print(process_priorities)
    
    # 찾고자하는 프로세스(알파벳)
    target_process = process_priorities[location][1]
    print("target_process : ", target_process)
    
    while True:
        current_process = process_priorities.popleft()
        
        # 현재 프로세스가 우선순위가 가장 높은지 확인
        is_highest_priority = True
        for item in process_priorities:
            if current_process[0] < item[0]:
                is_highest_priority = False
                break
        
        # 가장 높은 것일 경우 찾는 알파벳이 맞는지 검사
        if is_highest_priority:
            answer += 1
            if current_process[1] == target_process:
                return answer
        # 아니면 맨 뒤로 이동
        else:
            process_priorities.append(current_process)
        
    
    return answer