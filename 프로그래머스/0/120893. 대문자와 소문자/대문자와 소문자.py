def solution(my_string):
    answer = ''
    for letter in my_string:
        if 97 <= ord(letter) <= 122:
            answer += chr(ord(letter) - 32)
        if 65 <= ord(letter) <= 90:
            answer += chr(ord(letter) + 32)
#    print(ord("a")) 97
#    print(ord("z")) 122
#    print(ord("A")) 65
#    print(ord("Z")) 90
    return answer