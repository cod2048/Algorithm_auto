def solution(record):
    dic = {}
    log = []
    answer = []

    for command in record:
        separate_command = command.split()
        action = separate_command[0]
        user_id = separate_command[1]
        
        if action == "Enter" or action == "Change":
            dic[user_id] = separate_command[2]
        
        if action != "Change":
            log.append((action, user_id))
    
    for action, user_id in log:
        if action == "Enter":
            answer.append(f"{dic[user_id]}님이 들어왔습니다.")
        else:
            answer.append(f"{dic[user_id]}님이 나갔습니다.")
    
    return answer