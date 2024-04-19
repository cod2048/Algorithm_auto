def solution(myString, pat):
    max_length = 0
    longest_substring = ""

    # 현재 시작점부터 myString의 끝까지 슬라이싱
    for end in range(len(myString)+1):
        substring = myString[:end]
        # 부분 문자열이 pat으로 끝나는지 확인
        if substring.endswith(pat):
            # 가장 긴 부분 문자열을 갱신
            if len(substring) > max_length:
                max_length = len(substring)
                longest_substring = substring

    return longest_substring
