def solution(quiz):
    answer = []
    for i in quiz:
        expression = i.split(" = ")
        if eval(expression[0]) == int(expression[1]):
            answer.append("O")
        else:
            answer.append("X")
            
    
    return answer