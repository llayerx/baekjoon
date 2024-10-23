# https://www.acmicpc.net/problem/3009 네 번째 점

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.read().splitlines()

from collections import Counter

dots_x = []
dots_y = []

for row in INPUT:
    x, y = map(int, row.split())
    dots_x.append(x)
    dots_y.append(y)

x_count = Counter(dots_x)
y_count = Counter(dots_y)

min_x = [x for x in x_count if x_count[x] == 1][0]
min_y = [y for y in y_count if y_count[y] == 1][0]

print(f"{min_x} {min_y}")


# GPT --- #
# XOR 연산을 통해서, 한번만 등장한 좌표를 찾기

dots_x = []
dots_y = []

# 입력 받아서 x, y 좌표를 각각 리스트에 저장
for row in INPUT:
    x, y = map(int, row.split())
    dots_x.append(x)
    dots_y.append(y)

# x, y 좌표에서 2번 등장한 좌표는 버리고, 1번만 등장한 좌표를 찾기
min_x = dots_x[0] ^ dots_x[1] ^ dots_x[2]
min_y = dots_y[0] ^ dots_y[1] ^ dots_y[2]

# 결과 출력
print(f"{min_x} {min_y}")