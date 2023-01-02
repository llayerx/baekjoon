# https://www.acmicpc.net/problem/24060

def merge_sort(A, p, r):  # A[p..r]을 오름차순 정렬한다.
    print(f'sort from {p} to {r}, list {A}')
    if p < r:
        q = int((p + r) / 2)     
        print('here q', q)
        A = merge_sort(A, p, q)      # 전반부 정렬
        A = merge_sort(A, q + 1, r)  # 후반부 정렬
        A = merge(A, p, q, r);        # 병합
    return A

def merge(A, p, q, r):
    print('merge start', A, p, q, r)
    i = p
    j = q + 1 
    tmp = []
    while i <= q and j <= r: 
        if A[i] < A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    print('merge done', tmp)
    for i, j in zip(range(p, r), range(len(tmp))):
        A[i] = tmp[j]
    return A

import sys
sys.stdin = open('input.txt')

size, save_time = list(map(int, sys.stdin.readline().split()))
print(size, save_time)

lst = list(map(int, sys.stdin.readline().strip().split()))
print(lst)
lst2 = merge_sort(lst, 0, size)
print(lst2)