import sys
input = sys.stdin.readline
from collections import deque

# push_front : 정수x를 덱의 앞에 넣기
# push_back : 정수 X를 덱의 뒤에 넣기
# pop_front : 덱의 가장 앞에 수 빼고, 출력(없으면 -1)
# pop_back : 덱의 가장 뒤에 수 뺴고, 출력(없으면 -1)
# size: 덱에 있는 정수의 개수 출력
# empty: 덱이 비어있으면 1 아니면 0
# front : 가장 앞의 정수 출력(없으면 -1)
# back : 가장 뒤에 있는 정수 출력(없으면 -1)

N = int(input().strip())
q = deque()
push_command = ["push_back", "push_front"]
for _ in range(N):
    commands = input().split()
    command = commands[0]
    if command in push_command:
        number = commands[1]
    if command == "push_front":
        q.appendleft(number)    
    if command == "push_back":
        q.append(number)
    if command == "pop_front":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    if command == "pop_back":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    if command == "size":
        print(len(q))
    if command == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    if command == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    if command == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])

