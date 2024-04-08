def solution(arr, idx):
    answer = -1
    # idx보다 크면서 배열의 값이 1
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            answer = i
            break
    return answer