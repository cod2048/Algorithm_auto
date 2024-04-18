def solution(i, j, k):
    answer = 0
    for number in range(i, j + 1):
        for letter in str(number):
            if letter == str(k):
                answer += 1
    return answer