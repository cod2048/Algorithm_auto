def solution(rny_string):
    answer = ''
    for letter in rny_string:
        if letter == "m":
            answer += "rn"
        else:
            answer += letter
    return answer