import sys
input = sys.stdin.readline

N = int(input())
num_list = int(input())
answer = 0

for num in str(num_list):
    answer += int(num)

print(answer)