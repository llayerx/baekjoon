# https://www.acmicpc.net/problem/4948

import sys
sys.stdin = open('input.txt')

lst = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    lst.append(n)

end = max(lst) * 2
start = min(lst)

target = range(start + 1 if start%2==0 else start, end+1, 2)
prime = []
skip = set()

for i in range(3, end+1, 2):
    if i in skip:
        continue
    if i in target:
        prime.append(i)
    tmp = [i * x for x in range(1, end // i + 1)]
    skip.update(tmp)

for i in lst:
    count = 0
    if i <= 2:
        print(1)
        continue

    for p in prime:
        if p >= i*2:
            break
        if p > i:
            count += 1
    print(count)