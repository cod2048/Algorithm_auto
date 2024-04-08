def solution(strArr):
    answer = [strArr[0].lower()]
    for i in range(1, len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())
    return answer