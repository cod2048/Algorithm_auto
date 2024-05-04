def solution(s):
    low_alp = ""
    up_alp = ""
    for alp in s:
        if alp.isupper():
            up_alp += alp
        else:
            low_alp += alp
    
    answer = sorted(low_alp, reverse = True)
    answer += sorted(up_alp, reverse = True)
    
    return "".join(answer)