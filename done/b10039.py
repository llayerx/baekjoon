"""https://www.acmicpc.net/problem/10039 평균 점수"""

INPUT = """10
65
100
30
95"""

"""5명의 평균 점수를 계산해서 출력

Args:
    data (str): 5명의 평균점수 입력
"""
scores = list(map(int, INPUT.split()))
scores = [max(40, x) for x in scores]
result = sum(scores)/len(scores)
print(result)
