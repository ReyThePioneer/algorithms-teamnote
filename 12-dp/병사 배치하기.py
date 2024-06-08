# <문제> 병사 배치하기

# Q. n명의 병사를 전투력이 높은 병사부터 배치
# 남아있는 병사의 수를 최대로 하기 위해 열외시켜야 하는 병사의 수?

# A. 가장 긴 '감소'하는 부분 수열 찾기!
# 가장 긴 '증가'하는 부분 수열 알고리즘을 조금 수정하여 적용
# LIS (Longest Increasing Subsequence)
# 입력받은 병사 정보를 뒤집기

n = int(input()) # 7
array = list(map(int, input().split())) # 15 11 4 8 5 2 4

# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

# dp를 위한 1차원 dp table 초기화
dp = [1] * n

# 최장 증가 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수 출력
print(n - max(dp))