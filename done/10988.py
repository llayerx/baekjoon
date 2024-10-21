# https://www.acmicpc.net/problem/10988 팰린드롬인지 확인하기

import sys
# sys.stdin = open('input.txt')
INPUT = input()

result = 1
for a, b in zip(INPUT, INPUT[::-1]):
    if a != b:
        result = 0
        break
print(result)