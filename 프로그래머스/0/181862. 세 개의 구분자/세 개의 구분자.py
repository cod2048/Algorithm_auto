def solution(myStr):
    answer = []
    tmp = ''
    for letter in myStr:
        if letter == "a" or letter == "b" or letter == "c":
            if tmp == '':
                continue
            answer.append(tmp)
            tmp = ''
            continue
        else:
            tmp += letter
    
    if tmp != "":
        answer.append(tmp)
    
    if not answer:
        answer.append("EMPTY")
        
    return answer