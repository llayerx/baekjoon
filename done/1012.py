# https://www.acmicpc.net/problem/1012 유기농 배추

INPUT = """2
25 25 4
11 11
12 12
12 11
11 12
10 10 3
1 1
2 2
3 3""".split("\n")

import sys, itertools
# INPUT = sys.stdin.readlines()

def create_map(w, h, sp):
    grid = [[0] * w for _ in range(h)]
    for x, y in sp:
        grid[y][x] = 1
    return grid

def dfs(x, y):
    global grid, w, h
    
    if grid[y][x] != 1:
        return False
    
    check = [[x, y]]
    visited = set()
    while check:
        x, y = check.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if grid[y][x] == 1:
            grid[y][x] = 0 
            for sx, sy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx = x + sx
                ny = y + sy
                if nx < 0 or ny < 0 or nx >= w or ny >= h:
                    continue
                check.append([nx, ny])
    return True
    
def process_input(lines):
    global grid, w, h
    num_experiments = int(lines.pop(0))
    for i in range(num_experiments):
        w, h, num_sp = map(int, lines.pop(0).split())
        sp = [tuple(map(int, lines.pop(0).split())) for _ in range(num_sp)]
        grid = create_map(w, h, sp)
        count = 0
        for y, x in itertools.product(range(h), range(w)):
            if grid[y][x]:
                if dfs(x, y):
                    count += 1
        print(count)
    return 
process_input(INPUT)
