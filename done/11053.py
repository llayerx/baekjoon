# https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열

import sys
import io

INPUT = """6
10 20 10 30 20 50"""
sys.stdin = io.StringIO(INPUT)

length = int(input())
lst = list(map(int, input().split())) 

def length_of_LIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(length_of_LIS(lst))



## GPT 제안 코드
## 이진탐색을 사용한 LIS 알고리즘
from bisect import bisect_left

length = int(input())
lst = list(map(int, input().split()))

def length_of_LIS(nums):
    if not nums:
        return 0

    # tails 배열은 길이 i+1을 가진 LIS의 마지막 값의 최소 가능 값을 저장합니다.
    tails = []

    for num in nums:
        # 이진 탐색을 사용하여 tails에서 num의 위치를 찾습니다.
        # num이 tails의 모든 요소보다 큰 경우, num을 tails에 추가합니다.
        # 그렇지 않으면, num이 들어갈 적절한 위치를 찾아 업데이트합니다.
        index = bisect_left(tails, num)
        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num

    # tails 배열의 길이가 LIS의 길이와 동일합니다.
    return len(tails)

print(length_of_LIS(lst))
