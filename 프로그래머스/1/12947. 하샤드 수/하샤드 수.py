def solution(x):
    answer = False
    number = 0
    for num in str(x):
        number += int(num)
    
    if x % number == 0:
        answer = True
    return answer