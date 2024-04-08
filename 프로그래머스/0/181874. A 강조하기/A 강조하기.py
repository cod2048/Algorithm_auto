def solution(myString):
    answer = ''
    for letter in myString:
        if letter == "a" or letter == "A":
            answer += "A"
        else:
            answer += letter.lower()
    return answer