# https://www.acmicpc.net/problem/2839 설탕배달

order = int(input())

f = order // 5
while f >= 0:
    left = order - f * 5
    if left % 3 == 0:
        t = left // 3
        print(f + t)
        print(f'Five:{f}, Three:{t}')
        break
    f -= 1
    if f < 0:
        print(-1)
        print(f'Impossible')
