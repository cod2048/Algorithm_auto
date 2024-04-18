def solution(num, total):
    avg = total // num
    offset = num // 2
    end = avg + offset
    
    if num % 2 == 1:
        start = avg - offset    
    else:
        start = avg - offset + 1

    return list(range(start, end + 1))
