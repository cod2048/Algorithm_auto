def solution(board):
    answer = 0
    n = len(board)
    safe_board = [[0] * n for _ in range(n)]
    print(safe_board)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                safe_board[i][j] = 1
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0<= ny < n:
                        safe_board[nx][ny] = 1
    
    for i in range(n):
        for j in range(n):
            if safe_board[i][j] == 0:
                answer += 1
    
    return answer