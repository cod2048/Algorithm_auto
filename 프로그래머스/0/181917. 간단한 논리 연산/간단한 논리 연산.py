def solution(x1, x2, x3, x4):

    def down_calculation(x, y):
        if not x and not y:
            return False
        else:
            return True
    
    def up_calculation(x, y):
        if x and y:
            return True
        else:
            return False
    
    first_result = down_calculation(x1, x2)
    second_result = down_calculation(x3, x4)
    answer = up_calculation(first_result, second_result)
    
    return answer