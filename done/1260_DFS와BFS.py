# https://www.acmicpc.net/problem/1260

import sys
sys.stdin = open('input.txt')

from collections import deque


def bfs(now):
    box = deque([now])
    check = set()   
    while box:
        pop = box.popleft()
        if pop not in graph.keys():
            print(pop, end=' ')
            return
        if pop not in check:
            print(pop, end=' ')
            check.add(pop)
            box.extend([x for x in sorted(graph[pop]) if x not in check])

def dfs(now, check):
    if now not in graph.keys():
        print(now, end=' ')
        return
    if now not in check:
        print(now, end=' ')
        check.add(now)
    for v in sorted(graph[now]):
        if v not in check:
            dfs(v, check)

_, edges, start = map(int, sys.stdin.readline().strip().split())
lines = [sys.stdin.readline().strip() for _ in range(edges)]

graph = {}
for line in lines:
    k, v = map(int, line.split(' '))
    if k in graph.keys():
        graph[k].append(v)
    else:
        graph[k] = [v]
    if v in graph.keys():
        graph[v].append(k)
    else:
        graph[v] = [k]

check = set()
dfs(start, check)
print()
bfs(start)

