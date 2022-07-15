# https://www.acmicpc.net/problem/1978

num_input = int(input())
nlst = map(int, input().split())

def isPrime(n):
    if n < 3:  # 1->1 2->0
        return n % 2
    d = 3
    while d * d <= n:
        if n % d == 0:  # non-prime -? 1
            return 1
        d += 2
    return (n + 1) % 2  # prime -> 0

nlst = [isPrime(k) for k in nlst]
print(nlst)
print(nlst.count(0))
