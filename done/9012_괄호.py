# https://www.acmicpc.net/problem/9012

n = int(input())
for i in range(n):
    ps = input()
    vps = 0
    for i in range(len(ps)):
        if ps[i] == '(':
            vps += 1
        else:
            vps -= 1
        if vps < 0:
            break
    if vps == 0:
        print('YES')
    else:
        print('NO')




