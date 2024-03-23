def solution(sides):
    answer = 2
    longest_side = max(sides)
    other_sides = sum(sides) - longest_side
    if longest_side < other_sides:
        answer = 1
    return answer