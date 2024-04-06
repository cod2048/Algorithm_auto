def solution(order):
    answer = 0
    clap = ["3","6","9"]
    str_order = str(order)
    for number in str_order:
        if number in clap:
            answer += 1
    return answer