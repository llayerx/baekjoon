# https://www.acmicpc.net/problem/11718 그대로 출력하기

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()
for line in INPUT:
    print(line.strip())