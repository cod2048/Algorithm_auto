def solution(arr):
    lenght = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    while len(arr) not in lenght:
        arr.append(0)
    return arr