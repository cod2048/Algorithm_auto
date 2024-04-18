def solution(numbers):
    answer = ''
    num_list = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "zero" : 0}
    
    tmp = ''
    
    for char in numbers:
        if tmp in num_list.keys():
            answer += str(num_list[tmp])
            tmp = ''
        tmp += char
    
    if tmp:
        answer += str(num_list[tmp])

    
    return int(answer)