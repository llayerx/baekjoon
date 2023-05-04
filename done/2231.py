# https://www.acmicpc.net/problem/2231 분해합

import sys
sys.stdin = open('input.txt')
INPUT = int(sys.stdin.readlines()[0])
start = max(0, INPUT - (len(str(INPUT)))*9)  # 각 자릿수에서 최대 9를 더하니 아래로 그 범위만 탐색
for i in range(start, INPUT):
    res = i + sum(map(int, str(i)))
    if res == INPUT:
        print(i)
        break