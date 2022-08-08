# https://www.acmicpc.net/problem/2869
import math

goup, slip, height = map(int, input().split())
day = math.ceil((height - goup) / (goup - slip)) + 1
print(day)