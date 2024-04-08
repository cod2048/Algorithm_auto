def solution(n_str):
    i = 0
    while n_str[i] == "0":
        i += 1
    answer = n_str[i:]
    return answer