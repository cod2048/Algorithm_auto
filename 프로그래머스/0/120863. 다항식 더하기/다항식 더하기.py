def solution(polynomial):
    answer = ""
    divide = polynomial.split(" + ")
    num_x = 0
    num = 0

    for i in divide:
        if 'x' in i:
            plus = i.split('x')[0]
            if plus == '' or plus == '1':
                num_x += 1
            else:
                num_x += int(plus)
        else:
            num += int(i)
        
    if num_x == 0:
        answer = (f"{num}")
    elif num == 0:
        if num_x == 1:
            answer = "x"
        else:
            answer = (f"{num_x}x")
    else:
        if num_x == 1:
            answer = (f"x + {num}")
        else:
            answer = (f"{num_x}x + {num}")
            
    return answer