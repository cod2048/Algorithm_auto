def solution(arr):
    row = len(arr)
    col = len(arr[0])
    diff = abs(row - col)
    if row == col:
        return arr
    else:
        if row > col:
            for i in range(len(arr)):
                for _ in range(diff):
                    arr[i].append(0)
        else:
            tmp = [0 for i in range(col)]
            for _ in range(diff):
                arr.append(tmp)
            
    return arr