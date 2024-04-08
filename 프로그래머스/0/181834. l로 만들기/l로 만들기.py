def solution(myString):
    answer = ''
    # print(ord("l")) # 108
    for letter in myString:
        if ord(letter) < 108:
            answer += "l"
        else:
            answer += letter
    return answer