# https://www.acmicpc.net/problem/1920 수 찾기

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

lst = set(map(int, INPUT[1].strip().split()))
target = list(map(int, INPUT[3].strip().split()))

ans = []
for x in target:
    if x in lst:
        ans.append(1)
    else:
        ans.append(0)

print('\n'.join(map(str, ans)))