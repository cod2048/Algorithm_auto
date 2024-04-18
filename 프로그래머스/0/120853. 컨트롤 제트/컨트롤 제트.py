def solution(s):
    answer = []
    commands = s.split()
    
    for command in commands:
        if command == 'Z':
            answer.pop()
        else:
            answer.append(int(command))
    
    return sum(answer)