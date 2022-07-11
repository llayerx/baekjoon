# https://www.acmicpc.net/problem/2908

a, b = map(str, input().split())
rev_a, rev_b = int(a[::-1]), int(b[::-1])

print(rev_a) if rev_a > rev_b else print(rev_b)
