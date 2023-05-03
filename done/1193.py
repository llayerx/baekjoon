# https://www.acmicpc.net/problem/1193 분수찾기

n = int(input())
lvl = 1
while sum(range(lvl+1)) < n:
    lvl += 1
step = n - sum(range(lvl)) - 1
set = list(zip(range(lvl, 0, -1), range(1, lvl + 1)))
print(f'{set[step][(lvl + 1) % 2]}/{set[step][lvl % 2]}')


