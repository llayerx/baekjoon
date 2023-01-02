# https://www.acmicpc.net/problem/11651

import sys
sys.stdin = open('input.txt')

mt = {} 
mt = sys.stdin.readlines()[1:]
mt.sort(key=lambda x: (tuple(map(int, x.strip().split()))[::-1]))  # "X Y\n"의 개행 제거 후 공백분리해서 2개 기준(x, y)로 정렬
for pt in mt:
    print(pt.strip())
