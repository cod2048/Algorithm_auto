def solution(myString, pat):
    answer = 0
    result = ""
    for letter in myString:
        if letter == "A":
            result += "B"
        else:
            result += "A"
    if pat in result:
        answer = 1
    return answer