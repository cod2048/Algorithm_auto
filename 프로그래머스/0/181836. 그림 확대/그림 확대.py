def solution(picture, k):
    answer = []
    for row in picture:
        tmp = ""
        for letter in row:
            tmp += letter * k
        for _ in range(k):
            answer.append(tmp)
    return answer