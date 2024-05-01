def snail_graph(graph):
    n = len(graph)
    max_value = n * (n + 1) // 2
    number = 1
    x, y = 0, 0
    direction = "down"
    moves = {"down": (1, 0), "right": (0, 1), "up": (-1, -1)}

    graph[x][y] = number

    while number < max_value:
        nx, ny = x + moves[direction][0], y + moves[direction][1]

        if 0 <= nx < n and 0 <= ny <= nx and graph[nx][ny] == 0:
            x, y = nx, ny
            number += 1
            graph[x][y] = number
        else:
            if direction == "down":
                direction = "right"
            elif direction == "right":
                direction = "up"
            else:
                direction = "down"

def solution(n):
    answer = []
    graph = []
    
    for i in range(1, n+1):
        tmp = [0 for _ in range(i)]
        graph.append(tmp)
        
    snail_graph(graph)
    
    for i in range(n):
        for j in range(len(graph[i])):
            answer.append(graph[i][j])
    
    return answer