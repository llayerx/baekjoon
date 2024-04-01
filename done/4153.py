# https://www.acmicpc.net/problem/4153 직각삼각형

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

for line in INPUT[:-1]:
    nums = list(map(int, line.split()))
    nums.sort()
    pows = [x ** 2 for x in nums]
    if pows[2] == pows[1] + pows[0]:
        print('right')
    else:
        print('wrong')