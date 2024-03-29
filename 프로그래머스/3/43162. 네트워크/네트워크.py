from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            while queue:
                node = queue.popleft()
                visited[node] = True
                for j in range(n):
                    if computers[node][j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True
            answer += 1
    return answer
