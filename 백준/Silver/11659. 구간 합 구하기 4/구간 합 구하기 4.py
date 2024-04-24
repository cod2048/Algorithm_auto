import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
tmp = 0
sum_list = [0]

for num in numbers:
    tmp = tmp + num
    sum_list.append(tmp)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])