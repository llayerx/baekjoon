# https://www.acmicpc.net/problem/1929 소수 구하기

import sys
sys.stdin = open('input.txt')

start, end = map(int, sys.stdin.readline().split())
target = range(start + 1 if start%2==0 else start, end+1, 2)

skip = set()
if start < 3:
    print(2)

for i in range(3, end+1, 2):
    if i in skip:
        continue
    if i in target:
        print(i)

    tmp = [i * x for x in range(1, end // i + 1)]
    skip.update(tmp)
