from collections import deque

def solution(maps):
    answer = 0
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        # queue가 빌 때까지 반복 
        while queue:
            x, y = queue.popleft()
            
            # 상하좌우 칸 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵 범위 벗어나면 무시
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                    
                # 벽이면 무시
                if maps[nx][ny] == 0:
                    continue
                    
                # 처음 지나가는 길이면 지금 칸까지 거리계산 해서 갱신
                # 다시 상하좌우 확인
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
        # 상대 팀 진영(제일 오른 쪽 아래 칸) 까지의 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0, 0)
    return -1 if answer == 1 else answer