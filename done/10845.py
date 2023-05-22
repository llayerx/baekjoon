# https://www.acmicpc.net/problem/10845 큐

import sys

n = int(sys.stdin.readline().rstrip())
lst = []

for _ in range(n):
    command = sys.stdin.readline().rstrip().split(' ')
    if command[0] == 'push':
        lst.append(command[1])
    if command[0] == 'size':
        print(len(lst))
    if command[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    try:
        if command[0] == 'pop':
            print(lst.pop(0))
        if command[0] == 'front':
            print(lst[0])
        if command[0] == 'back':
            print(lst[-1])
    except:
        print(-1)