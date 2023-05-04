# https://www.acmicpc.net/problem/2606 바이러스

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

connections = INPUT[2:]

all = dict()
for c in connections:
    com1, com2 = map(int, c.strip().split())
    all[com1] = all.get(com1, []) + [com2]
    all[com2] = all.get(com2, []) + [com1]
    
see = [1]
visited = set()

while see:
    check = see.pop()
    visited.add(check)
    for node in all.get(check, []):
        if node not in visited:
            see.append(node)
            
print(len(visited)-1)
print(all) 