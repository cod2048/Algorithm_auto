def solution(s):
    answer = len(s)
    # 문자열길이의 절반 + 1까지 반복이 가능한지 검사
    # 제일 짧은 변수를 문자열 길이로 초기화
    # 더 짧은걸 찾으면 갱신
    for x in range(1, len(s) // 2 + 1):
        comp_len = 0
        comp = ''
        cnt = 1
        for i in range(0, len(s) + 1, x):
            tmp = s[i:i + x]
            if comp == tmp:
                cnt += 1
            elif comp != tmp:
                comp_len += len(tmp)
                if cnt > 1:
                    comp_len += len(str(cnt))
                cnt = 1
                comp = tmp
        answer = min(answer, comp_len)
        
    return answer