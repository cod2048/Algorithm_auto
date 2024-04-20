def solution(dots):
    dots.sort()
    x = abs(dots[2][0] - dots[0][0])
    y = abs(dots[1][1] - dots[0][1])
    return x*y