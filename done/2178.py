# https://www.acmicpc.net/problem/2178 미로 탐색

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

goal = list(map(int, INPUT[0].split()))
MAP = [list(map(int, x.strip())) for x in INPUT[1:]]
STEP = [[0 for _ in range(len(MAP[0]))] for _ in range(len(MAP))]

def check_valid(pos):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(MAP[0]) or pos[1] >= len(MAP)

move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

bfs = [[0, 0]]
STEP[0][0] = 1

while bfs:
    pos = bfs.pop(0)
    for step in move:
        new_pos = [a+b for a, b in zip(pos, step)]
        if check_valid(new_pos):
            continue
        if MAP[new_pos[1]][new_pos[0]] == 1 and STEP[new_pos[1]][new_pos[0]] == 0:
            STEP[new_pos[1]][new_pos[0]] = 1 + STEP[pos[1]][pos[0]]
            bfs.append(new_pos)

for l in STEP:  # Show MAP
    print(l)    
    
print(STEP[goal[0]-1][goal[1]-1])