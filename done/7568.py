# https://www.acmicpc.net/problem/7568 덩치

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

group = INPUT[1:]
lst = [list(map(int, x.strip().split(' '))) for x in group]

def count_big(x, lst):
    xw, xh = x
    count = 1
    for yw, yh in lst:
        if yw > xw and yh > xh:
            count += 1
    return count

print(' '.join(str(count_big(x, lst)) for x in lst))



# # 좌표명면 만드는 방식. 같은 부분이 있으면 비교불가라는 조건에 따라 틀린 접근...
# group = INPUT[1:]
# lst = [list(map(int, x.strip().split(' '))) for x in group]

# w, h = zip(*lst)  # 좌표평면 생성
# min_w = min(w)
# min_h = min(h)
# max_w = max(w) + 1
# max_h = max(h) + 1

# pmap = [[0 for _ in range(max_h-min_h)] for _ in range(max_w-min_w)]

# for w, h in lst:  # 사람을 1로
#     pmap[w-min_w][h-min_h] = 1
    
# for l in pmap:
#     print(l)

# for i in range(max_w-1-min_w, -1, -1):  # 사이즈를 비교해서 랭크 생성
#     for j in range(max_h-1-min_h, -1, -1):
#         down = pmap[i+1][j] if i+1 < max_w-min_w else 0
#         right = pmap[i][j+1] if j+1 < max_h-min_h else 0
#         add = max(down, right)
#         pmap[i][j] += add
        
# cluster = []
# for w, h in lst:
#     me = pmap[w-min_w][h-min_h]
#     cluster.append(me)
    
# rank = [1 + sum(x < y for x in cluster) for y in cluster]
# print(' '.join(str(x) for x in rank))

# for l in pmap:
#     print(l)
