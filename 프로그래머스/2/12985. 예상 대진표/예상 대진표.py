def nextNum(number):
    if number % 2 == 0:
        returnNum = number // 2
    else:
        returnNum = number // 2 + 1
    return returnNum

def solution(n,a,b):
    answer = 1
    while True:
        if a // 2 != b // 2 and abs(a-b) == 1:
            break
        
        answer += 1
        a = nextNum(a)
        b = nextNum(b)

    return answer