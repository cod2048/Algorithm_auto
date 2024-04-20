def solution(M, N):
    answer = 0
    if M == 1 and N == 1:
        return 0
    elif M == 1:
        return N - 1
    elif N == 1:
        return M - 1
    row = min(M, N)
    col = max(M, N)
    answer += row - 1
    answer += (col - 1) * row
    return answer