def solution(myString):
    split_strings = [s for s in myString.split("x") if s]
    sorted_array = sorted(split_strings)
    return sorted_array