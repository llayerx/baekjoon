# https://www.acmicpc.net/problem/1017 소수쌍

import sys
import math
from itertools import combinations

sys.stdin = open('input.txt')

def isPrime(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))


