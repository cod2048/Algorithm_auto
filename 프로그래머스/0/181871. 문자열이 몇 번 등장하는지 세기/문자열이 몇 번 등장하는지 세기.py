def solution(myString, pat):
    answer = 0
    start = 0
    end = len(pat) - 1
    while end != len(myString):
        if myString[start:end + 1] == pat:
            answer += 1
        start += 1
        end += 1
    return answer