# https://www.acmicpc.net/problem/2798

from itertools import combinations

num, target = map(int, input().split())
lst = map(int, input().split())

comb = sorted(filter(lambda x: sum(x) <= target ,combinations(lst, 3)), key=sum)
print(sum(comb[-1]))


