# https://www.acmicpc.net/problem/10250
import math
step = 1#int(input())
for i in range(step):
    H, W, N = map(int, input().split())
    print(f'{N%H if N%H else H}{math.ceil(N/H):02d}')

