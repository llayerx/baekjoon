# https://www.acmicpc.net/problem/2581

def isPrimeList(lst):
    tmp = lst.copy()
    m, n = lst[0], lst[-1]

    if n < 3:  # 1->1 2->0
        tmp = [k % 2 for k in lst]

    lst = [k % 2 for k in lst]  # even -> 0
    d = 3
    while d * d <= n:
        lst = [(1 if k % d == 0 else k) for k in lst]  # 0 if not prime
        d += 2
    return lst

m, n = map(int, input().split())

nlst = [k for k in range(m, n + 1)]
print(nlst)
print(isPrimeList(nlst))

