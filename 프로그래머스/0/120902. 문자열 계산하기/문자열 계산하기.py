def solution(my_string):
    commands = my_string.split()
    answer = int(commands[0])
    for i in range(len(commands)):
        if commands[i] == "+":
            answer += int(commands[i + 1])
        elif commands[i] == "-":
            answer -= int(commands[i + 1])
        else:
            continue
    
    return answer