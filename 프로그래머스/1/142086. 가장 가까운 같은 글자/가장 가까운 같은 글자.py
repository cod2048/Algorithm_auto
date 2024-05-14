def solution(s):
    answer = [-1]
    
    for i in range(1, len(s)):
        target_letter = s[i]
        result = -1
        
        for j in range(i):
            if s[j] == target_letter:
                result = j
        
        if result != -1:
            answer.append(i-result)
        else:
            answer.append(result)
        
    return answer