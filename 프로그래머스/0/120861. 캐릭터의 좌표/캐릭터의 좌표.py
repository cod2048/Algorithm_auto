def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput:
        if i == "left":
            if board[0] // 2 < abs(answer[0] - 1):
                continue
            answer[0] -= 1
        elif i == "right":
            if board[0] // 2 < abs(answer[0] + 1):
                continue
            answer[0] += 1
        elif i == "up":
            if board[1] // 2 < abs(answer[1] + 1):
                continue
            answer[1] += 1
        else:
            if board[1] // 2 < abs(answer[1] - 1):
                continue
            answer[1] -= 1
    return answer