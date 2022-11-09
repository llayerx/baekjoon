# https://www.acmicpc.net/problem/1463

n = int(input())
lst = [0, 0, 1, 1] + [1000 for _ in range(n-3)]
for i in range(4, n+1):
    candi = [lst[i-1]]
    if i % 2 == 0:
        candi.append(lst[int(i/2)])
    if i % 3 == 0:
        candi.append(lst[int(i/3)])
    lst[i] = min(candi) + 1
print(lst[n])
