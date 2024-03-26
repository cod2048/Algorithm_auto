def solution(my_string):
    answer = ''
    moeum = ['a','e','i','o','u']
    for letter in my_string:
        if letter not in moeum:
            answer += letter
    return answer