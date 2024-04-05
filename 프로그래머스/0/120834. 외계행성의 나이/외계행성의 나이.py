def solution(age):
    answer = ''
    age_dic = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}
    str_age = str(age)
    for letter in str_age:
        answer += age_dic[int(letter)]
    return answer