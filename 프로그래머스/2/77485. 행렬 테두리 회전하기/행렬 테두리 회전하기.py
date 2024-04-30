def rotate_graph(graph, query):
    x1 = query[0]-1
    y1 = query[1]-1
    x2 = query[2]-1
    y2 = query[3]-1
    
    tmp = graph[x1][y1]
    min_value = tmp
    
    for x in range(x1, x2):
        graph[x][y1] = graph[x + 1][y1]
        min_value = min(min_value, graph[x + 1][y1])
        
    for y in range(y1, y2):
        graph[x2][y] = graph[x2][y + 1]
        min_value = min(min_value, graph[x2][y + 1])
    
    for x in range(x2, x1, -1):
        graph[x][y2] = graph[x - 1][y2]
        min_value = min(min_value, graph[x - 1][y2])
    
    for y in range(y2, y1 + 1, -1):
        graph[x1][y] = graph[x1][y - 1]
        min_value = min(min_value, graph[x1][y - 1])
        
    graph[x1][y1 + 1] = tmp

    return min_value

def solution(rows, columns, queries):
    answer = []
    graph = []
    
    for i in range(rows):
        tmp = []
        
        for j in range(columns):
            tmp.append(i * columns + (j + 1))
            
        graph.append(tmp)
    
    for query in queries:
        answer.append(rotate_graph(graph, query))
        
    return answer