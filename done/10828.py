# https://www.acmicpc.net/problem/10828 스택

import sys

n = int(input())
stack = []

for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd[:2] == 'pu':
        num = cmd.split(' ')[-1]
        stack.append(num)
    elif cmd[0] == 'p':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 's':
        print(len(stack))
    elif cmd[0] == 'e':
        print(0) if len(stack) > 0 else print(1)
    else:
        print(stack[-1]) if stack else print(-1)
    
        


