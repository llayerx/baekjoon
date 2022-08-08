# https://www.acmicpc.net/problem/2292

target = int(input())
rad, rank = 1, 0
while 1:
    rad += rank * 6
    if target <= rad:
        print(rank+1)
        break
    rank += 1
