# https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열

import sys
import io

INPUT = """6
10 20 10 30 20 50"""
sys.stdin = io.StringIO(INPUT)

lst = list(map(int, sys.stdin.readlines()[-1].split()))

print(lst)