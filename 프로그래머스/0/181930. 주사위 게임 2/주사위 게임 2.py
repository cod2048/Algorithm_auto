def solution(a, b, c):
    answer = 0
    if a == b == c:
        answer += (a+b+c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)
    elif a == b != c or a != b == c or a == c != b:
        answer += (a+b+c) * (a*a + b*b + c*c)
    else:
        answer += a+b+c
    
    
    return answer