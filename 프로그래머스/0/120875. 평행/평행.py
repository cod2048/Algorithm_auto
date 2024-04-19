def solution(dots):
    case1_1 = abs(dots[0][1] - dots[1][1]) / abs(dots[0][0] - dots[1][0])
    case1_2 = abs(dots[3][1] - dots[2][1]) / abs(dots[3][0] - dots[2][0])
    if case1_1 == case1_2:
        return 1
    
    case2_1 = abs(dots[0][1] - dots[2][1]) / abs(dots[0][0] - dots[2][0])
    case2_2 = abs(dots[3][1] - dots[1][1]) / abs(dots[3][0] - dots[1][0])
    if case2_1 == case2_2:
        return 1
    
    case3_1 = abs(dots[0][1] - dots[3][1]) / abs(dots[0][0] - dots[3][0])
    case3_2 = abs(dots[2][1] - dots[1][1]) / abs(dots[2][0] - dots[1][0])
    if case3_1 == case3_2:
        return 1
        
    return 0