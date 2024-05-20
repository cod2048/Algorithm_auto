def solution(s):
    answer = [0, 0]
    
    while True:
        if s == "1":
            break
            
        answer[0] += 1
        zero = s.count("0")
        answer[1] += zero
        s = s.replace("0", "")
        
        length = len(s)
        new_s = ""
        
        while length > 0:
            new_s += str(length % 2)
            length = length // 2
        
        s = new_s[::-1]
    

    return answer