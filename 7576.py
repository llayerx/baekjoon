# https://www.acmicpc.net/problem/7576 토마토

INPUT = """""".split("\n")

with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()
    
import sys
INPUT = sys.stdin.readlines()

M, N = map(int, INPUT[0].split())
box = [[int(x) for x in y.split(' ')] for y in INPUT[1:]]

from collections import deque

# 익은 토마토 위치 찾기
dq = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            dq.append((i, j, 0))

# BFS 알고리즘 적용
days = 0
while dq:
    i, j, d = dq.popleft()
    days = max(days, d)  # 최소 일수 갱신
    for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        if 0 <= ni < N and 0 <= nj < M and box[ni][nj] == 0:
            box[ni][nj] = 1  # 익은 토마토로 바꾸기
            dq.append((ni, nj, d+1))

# 모든 토마토가 익는 최소 일수 출력
for row in box:
    if 0 in row:
        print(-1)
        break
else:
    print(days)
