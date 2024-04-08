def solution(str_list, ex):
    answer = ''
    for letter in str_list:
        if ex in letter:
            continue
        answer += letter
    return answer