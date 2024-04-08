def solution(myString):
    answer = []
    result = myString.split("x")
    for word in result:
        answer.append(len(word))
    return answer