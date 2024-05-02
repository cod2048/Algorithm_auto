def keep_distance(place):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for x in range(5):
        for y in range(5):
            if place[x][y] == 'P':
                # 바로 옆칸 검사
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == 'P':  # 바로 옆에 사람이 있는 경우
                            return 0
                        elif place[nx][ny] == 'O':  # 빈 테이블이면 다음 칸도 검사
                            nnx, nny = nx + dx, ny + dy
                            if 0 <= nnx < 5 and 0 <= nny < 5 and place[nnx][nny] == 'P':
                                return 0
                
                # 대각선 검사
                for dx, dy in diagonal:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] == 'P':
                        if place[x][ny] != 'X' or place[nx][y] != 'X':
                            return 0

    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(keep_distance(place))
        
    return answer
