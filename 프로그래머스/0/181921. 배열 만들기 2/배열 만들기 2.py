def solution(l, r):
    answer = []

    for num in range(l, r + 1):
        str_num = str(num)
        valid = True
        for char in str_num:
            if char != '0' and char != '5':
                valid = False
                break
        if valid:
            answer.append(num)

    if not answer:
        answer.append(-1)
    
    return answer