def solution(s):
    answer = True
    stk = []
    
    for bracket in s:
        if bracket == ")":
            if len(stk) == 0 or stk[-1] == ")":
                answer = False
                break
            elif stk[-1] == "(":
                stk.pop()
                
        else:
            stk.append("(")

    if len(stk) != 0:
        answer = False

    return answer