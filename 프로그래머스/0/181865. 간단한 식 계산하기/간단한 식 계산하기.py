def solution(binomial):
    answer = 0
    fomula = binomial.split()
    first_num = fomula[0]
    second_num = fomula[-1]
    if fomula[1] == "+":
        answer = int(first_num) + int(second_num)
    elif fomula[1] == "-":
        answer = int(first_num) - int(second_num)
    else:
        answer = int(first_num) * int(second_num)
    return answer