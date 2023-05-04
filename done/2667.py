# https://www.acmicpc.net/problem/2667 단지번호붙이기

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

MAP = [[int(a) for a in lst.strip()] for lst in map(str, INPUT[1:])]
MAX_SIZE = int(INPUT[0])

def dfs(x, y):
    if x < 0 or y < 0 or x >= MAX_SIZE or y >= MAX_SIZE:
        return 0
    if MAP[x][y] == 1:
        cnt = 1
        MAP[x][y] = 0 
        cnt +=dfs(x-1, y)
        cnt +=dfs(x, y-1)
        cnt +=dfs(x+1, y)
        cnt +=dfs(x, y+1)
        return cnt
    return 0

counts = []
for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        cnt = dfs(i, j)
        if cnt:
            counts.append(cnt)
            cnt = 0
            
print(len(counts))
for i in sorted(counts):
    print(i)