def solution(num_list):
    answer = 0
    result_a = 1
    result_b = 0
    for num in num_list:
        result_a *= num
    result_b = sum(num_list)*sum(num_list)
    return 1 if result_a < result_b else 0