# https://www.acmicpc.net/problem/1874 스택 수열

import sys
import io

INPUT = """8
4
3
6
8
7
5
2
1"""

sys.stdin = io.StringIO(INPUT)

MAX = int(sys.stdin.readline())

target = []
for i in range(MAX):
    target.append(int(sys.stdin.readline()))
    
stack = []
result = []
current = 1

for num in target:
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        sys.exit()

for op in result:
    print(op)
    
    
    