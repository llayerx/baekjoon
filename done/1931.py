# https://www.acmicpc.net/problem/1931 회의실 배정

import sys
INPUT = sys.stdin.readlines()
meets = [[int(x) for x in y.split(' ')] for y in INPUT[1:]]
meets.sort(key=lambda x: (x[1], x[0]))

last_end_time = -1
count = 0

for start, end in meets:
    print(f'{start} -> {end}')
    if start >= last_end_time:
        count += 1
        last_end_time = end
print(count)