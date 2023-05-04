# https://www.acmicpc.net/problem/1085 직사각형에서 탈출

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()[0].split(' ')
x, y, w, h = map(int, INPUT)

min_h = min(abs(x - w), x)
min_w = min(abs(y - h), y)

ans = min(min_h, min_w)
print(ans)