# https://www.acmicpc.net/problem/2775

case = int(input())

for _ in range(case):
    floor = int(input())
    room = int(input())
    print(f'Find {floor}F {room}R')

    f1st = [k for k in range(1, room + 1)]
    print(f1st)
    for i in range(floor):
        f1st = [sum(f1st[:k]) for k in range(1, room + 1)]
        print(f1st)
    print(f1st[-1])