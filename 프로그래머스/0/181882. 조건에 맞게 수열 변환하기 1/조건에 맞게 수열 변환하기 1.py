def solution(arr):
    answer = []
    for num in arr:
        if num >= 50 and num % 2== 0:
            answer.append(num // 2)
            continue
        if num < 50 and num % 2 == 1:
            answer.append(num * 2)
            continue
        answer.append(num)
        
    return answer