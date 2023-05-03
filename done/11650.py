# https://www.acmicpc.net/problem/11650 좌표 정렬하기

import sys
sys.stdin = open('input.txt')

mt = {} 
mt = sys.stdin.readlines()[1:]  # 첫줄 제거
mt.sort(key=lambda x: (tuple(map(int, x.strip().split()))))  # "X Y\n"의 개행 제거 후 공백분리해서 2개 기준(x, y)로 정렬
for pt in mt:  # 출력 형식 맞추기
    print(pt[:-1])  # 개행 제거
