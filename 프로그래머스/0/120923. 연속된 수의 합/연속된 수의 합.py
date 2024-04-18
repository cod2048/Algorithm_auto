def solution(num, total):
    avg = total // num
    offset = num // 2
    
    if num % 2 == 1:
        start = avg - offset
        end = avg + offset
    else:
        start = avg - offset + 1
        end = avg + offset

    return list(range(start, end + 1))
