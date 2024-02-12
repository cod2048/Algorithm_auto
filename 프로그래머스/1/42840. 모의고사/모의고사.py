def solution(answers):
    answer = []
    
    case1 = [1,2,3,4,5]
    case2 = [2,1,2,3,2,4,2,5]
    case3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0]*3
    
    for i in range(len(answers)):
        if answers[i] == case1[i%5]:
            scores[0] += 1
            
        if answers[i] == case2[i%8]:
            scores[1] += 1
            
        if answers[i] == case3[i%10]:
            scores[2] += 1
        
    for i in range(len(scores)):
        if scores[i] == max(scores):
            answer.append(i + 1)

    
    return answer