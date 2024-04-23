def solution(numlist, n):
    answer = []
    sorted_by_n = []
    for num in numlist:
        sorted_by_n.append([num, abs(num-n)])
    
    sorted_by_n.sort(key = lambda x : (x[1], -x[0]))
    for num in sorted_by_n:
        answer.append(num[0])
    return answer