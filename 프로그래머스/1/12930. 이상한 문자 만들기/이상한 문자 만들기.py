def solution(s):
    answer = ''
    idx = 2
    
    for letter in s:
        
        if letter == " ":
            answer += letter
            idx = 2
            continue
            
        if idx % 2 == 0:
            answer += letter.upper()
        else:
            answer += letter.lower()
        idx += 1
            
    return answer