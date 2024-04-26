def solution(s):
    answer = True
    lower_s = s.lower()

    count_p = 0
    count_y = 0
    
    for letter in lower_s:
        if letter == "p":
            count_p += 1
        elif letter == "y":
            count_y += 1
    
    if count_p == 0 and count_y == 0:
        return answer
    
    if count_p != count_y:
        answer = False

    return answer