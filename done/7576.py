# https://www.acmicpc.net/problem/7576 토마토

import sys
INPUT = sys.stdin.readlines()

M, N = map(int, INPUT[0].split())
box = [[int(x) for x in y.split(' ')] for y in INPUT[1:]]

from collections import deque

queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j, 0))

days = 0
while queue:
    i, j, d = queue.popleft()
    days = d
    for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        if 0 <= ni < N and 0 <= nj < M and box[ni][nj] == 0:
            box[ni][nj] = 1
            queue.append((ni, nj, d+1))

for row in box:
    if 0 in row:
        print(-1)
        break
else:
    print(days)