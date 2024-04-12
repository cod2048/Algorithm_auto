str = input()
answer = ''
for letter in str:
    if letter.isupper():
        answer += letter.lower()
    else:
        answer += letter.upper()

print(answer)