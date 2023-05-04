# https://www.acmicpc.net/problem/2920 음계

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

code = INPUT[0].split(' ')
if code == sorted(code):
    print('ascending')
elif code == sorted(code, reverse=True):
    print('descending')
else:
    print('mixed')