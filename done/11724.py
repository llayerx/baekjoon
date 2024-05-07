# https://www.acmicpc.net/problem/11724 연결 요소의 개수

"""6 5
1 2
2 5
5 1
3 4
4 6"""

import sys
sys.stdin = open('input.txt')

# --- GPT UNION_FIND 방식 ---

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

INPUT = sys.stdin.readlines()

NODES, _ = map(int, INPUT[0].split())

root = [i for i in range(NODES+1)]
rank = [0] * (NODES + 1)

for line in INPUT[1:]:
    a, b = map(int, line.split())
    union(root, rank, a, b)

root_set = set(find(root, i) for i in range(1, NODES + 1))
print(len(root_set))
