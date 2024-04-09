def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        tmp = int(intStrs[i][s:s+l])
        if tmp > k:
            answer.append(tmp)
    return answer