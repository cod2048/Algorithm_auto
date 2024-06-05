def solution(food):
    answer = ''
    result = ''
    for i in range(1,len(food)):
        tmp = food[i] // 2
        result += str(i) * tmp
        
    answer += result
    answer += "0"
    answer += result[::-1]
    return answer