def solution(s):
    answer = ""
    idx = 0
    
    for letter in s:
        if letter == " ":
            idx = 0
            answer = answer + " "
            
        else:
            if idx == 0:
                answer = answer + letter.upper()
                idx = 1
                continue
            
            else:
                answer = answer + letter.lower()
                
            
                
            
    
    return answer