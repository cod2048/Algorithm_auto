def solution(str_list):
    if "l" in str_list and "r" in str_list:
        l_index = str_list.index("l")
        r_index = str_list.index("r")
        if l_index < r_index:  # "l"이 "r"보다 먼저 나오면
            return str_list[:l_index]
        else:  # "r"이 "l"보다 먼저 나오면
            return str_list[r_index+1:]
    elif "l" in str_list:  # 리스트에만 "l"이 있을 경우
        return str_list[:str_list.index("l")]
    elif "r" in str_list:  # 리스트에만 "r"이 있을 경우
        return str_list[str_list.index("r")+1:]
    else:  # "l"이나 "r"이 없는 경우
        return []
