# https://www.acmicpc.net/problem/10866 덱

"""15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front"""

from collections import deque
import sys

sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

result = deque()

for line in INPUT[1:]:
    if line[:4] == 'push':
        op, num = line.split()
    else:
        op = line.replace('\n', '')
        
    if op == 'push_front':
        result.appendleft(int(num))
    elif op == 'push_back':
        result.append(int(num))
    elif op == 'pop_front':
        if any(result):
            print(result.popleft())
        else:
            print(-1)
    elif op == 'pop_back':
        if any(result):
            print(result.pop())
        else:
            print(-1)
    elif op == 'size':
        print(len(result))
    elif op == 'empty':
        print(0 if len(result) else 1)
    elif op == 'front':
        print(result[0] if result else -1)
    elif op == 'back':
        print(result[-1] if result else -1)
