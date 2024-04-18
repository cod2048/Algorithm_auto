def solution(common):
    answer = 0
    minus = common[-1] - common[-2]
    if common[-1] - common[-2] == common[-2] - common[-3]:
        answer = common[-1] + minus
    else:
        answer = common[-1] * (common[-1] // common[-2])
    return answer