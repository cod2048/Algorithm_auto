def solution(s):
    answer = ''
    tmp = ''
    number = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    
    for letter in s:
        if letter.isalpha():
            tmp += letter
            if tmp in number:
                answer += str(number[tmp])
                tmp = ""
        else:
            answer += letter
                
    return int(answer)