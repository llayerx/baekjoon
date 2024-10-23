# https://www.acmicpc.net/problem/25206 너의 평점은

import sys
sys.stdin = open('input.txt')

grade = {
    "A+":	4.5,
    "A0":	4.0,
    "B+":	3.5,
    "B0":	3.0,
    "C+":	2.5,
    "C0":	2.0,
    "D+":	1.5,
    "D0":	1.0,
    "F":	0.0
}

IN = sys.stdin.read().splitlines()
SUM = []
d = 0

for row in IN:
    sub, pt, g = row.split()
    if g == "P":
        continue
    SUM.append(float(pt) * grade[g])
    d += float(pt)
    
print(f"{sum(SUM)/d:.6f}")
        