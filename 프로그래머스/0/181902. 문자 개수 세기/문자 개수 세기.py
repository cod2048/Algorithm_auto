def solution(my_string):
    answer = [0 for i in range(52)]
    print(ord("a"))
    print(ord("z"))
    print(ord("A"))
    print(ord("Z"))
    
    
    for letter in my_string:
        if letter.isupper():
            answer[ord(letter) - 65] += 1
        if letter.islower():
            answer[ord(letter) - 71] += 1

    return answer