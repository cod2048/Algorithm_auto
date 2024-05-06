def solution(s, n):
    answer = ''
    for letter in s:
        if letter.islower():  # 소문자인 경우
            new_letter = chr((ord(letter) - ord('a') + n) % 26 + ord('a'))
        elif letter.isupper():  # 대문자인 경우
            new_letter = chr((ord(letter) - ord('A') + n) % 26 + ord('A'))
        else:  # 공백인 경우
            new_letter = letter
        answer += new_letter
    return answer
