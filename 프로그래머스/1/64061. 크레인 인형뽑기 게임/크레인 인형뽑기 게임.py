def solution(board, moves):
    stack = []
    answer = 0
    
    for i in moves:
        for j in range(len(board[i-1])):
            doll = board[j][i-1]
            if doll != 0:
                board[j][i-1] = 0
                if stack and stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
                break                
    
    return answer