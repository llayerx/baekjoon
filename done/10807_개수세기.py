# https://www.acmicpc.net/problem/10807

import sys
sys.stdin = open('input.txt')

_ = int(input())
nums = list(map(int, sys.stdin.readline().split(' ')))
target = int(input())

print(nums.count(target))