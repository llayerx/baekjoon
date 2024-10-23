# https://www.acmicpc.net/problem/10798 세로읽기

import sys
sys.stdin = open('input.txt')

IN = sys.stdin.read().splitlines()
print(IN)

result = []

for j in range(15):
    for i in range(5):
        if len(IN[i]) > j:
            result.append(IN[i][j])

print("".join(result))