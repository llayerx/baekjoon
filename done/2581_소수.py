# https://www.acmicpc.net/problem/2581
import math

def isPrime(n):
    if n < 3:  # 1->0 2->1
        return (n + 1) % 2
    if n % 2 == 0:  # even -> 0
        return 0

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:  # non-prime -? 0
            return 0
    return 1  # prime

m = int(input())
n = int(input())

rst = [0, 0]
for k in range(m, n+1):
    if isPrime(k):
        if rst[0] == 0:
            rst[0] = k
        rst[1] += k

if rst[0] > 0:
    print(f'{rst[1]}\n{rst[0]}')
else:
    print('-1')

# m = int(input())
# n = int(input())
#
# nlst = [k for k in range(m, n + 1)]
# tmp = []
#
# for i in nlst:
#     if i in [2, 3, 5, 7]:
#         tmp.append(i)
#
#     for j in range(11, i, 2):
#         if i % j == 0:
#             break
#         else:
#             tmp.append(i)
#
# if tmp:
#     print(sum(tmp))
#     print(min(tmp))
# else:
#     print('-1')
