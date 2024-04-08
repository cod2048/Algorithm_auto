def solution(a, b):
    result_a = int(str(a)+str(b))
    result_b = int(str(b)+str(a))
    return result_a if result_a > result_b else result_b