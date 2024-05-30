def solution(citations):
    answer = 0
    # thesis_cnt = len(citations)
    citations.sort(reverse = True)
    
    for idx, thesis in enumerate(citations):
        print(idx, thesis)
        if thesis >= idx + 1:
            answer = idx + 1
        else:
            break

    return answer