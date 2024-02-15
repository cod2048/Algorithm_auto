def solution(dirs):
    visited = set()
    x, y = 0, 0
    
    dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
    dy = {'U': 1, 'D': -1, 'L': 0, 'R': 0}
    
    for d in dirs:
        # 다음 위치 계산
        nx = x + dx[d]
        ny = y + dy[d]
        
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
        
        visited.add((x, y, nx, ny))
        visited.add((nx, ny, x, y))
        
        x, y = nx, ny
    
    return len(visited) // 2