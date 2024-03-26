""" https://www.acmicpc.net/problem/1697 숨바꼭질 """

from collections import deque

INPUT = """1 1"""

start, end = map(int, INPUT.split())

if start == end:
    print(0)
else:
    bfs = deque()
    bfs.append((start, 0))

    visited = set()
    visited.add(start)

    while bfs:
        pos, step = bfs.popleft()
        if pos == end:
            print(step)
            break

        for next_pos in (pos * 2, pos - 1, pos + 1):
            if 0 <= next_pos <= 100000 and next_pos not in visited:
                visited.add(next_pos)
                bfs.append((next_pos, step + 1))
