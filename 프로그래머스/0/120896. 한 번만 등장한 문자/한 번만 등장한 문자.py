def solution(s):
    answer = ''
    set_s = set(s)
    tmp = {}
    
    for char in set_s:
        tmp[char] = 0
        
    for char in s:
        tmp[char] += 1
        
    for char in tmp:
        if tmp[char] == 1:
            answer += char
    
    answer = sorted(answer)
    
    return ''.join(answer)