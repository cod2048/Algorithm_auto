import heapq

def solution(A, B):
    answer = 0
    heapq.heapify(A)
    
    heapq_B = [-num for num in B]
    heapq.heapify(heapq_B)
    
    for _ in range(len(A)):
        tmp = heapq.heappop(A) * -heapq.heappop(heapq_B)
        answer += tmp

    return answer