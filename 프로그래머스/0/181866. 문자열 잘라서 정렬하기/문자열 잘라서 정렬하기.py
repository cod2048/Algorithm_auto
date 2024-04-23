def solution(myString):
    answer = myString.split('x')
    without_spaces = [x for x in answer if x]
    without_spaces.sort()
    return without_spaces