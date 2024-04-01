# https://www.acmicpc.net/problem/15649 N과 M (1)

from itertools import permutations

a, b = input().split()

pool = range(1, int(a)+1)

lst = permutations(pool, int(b))
for pair in lst:
    print(' '.join(list(map(str, pair))))
