def solution(arr, delete_list):
    answer = []
    for number in arr:
        if number not in delete_list:
            answer.append(number)
    return answer