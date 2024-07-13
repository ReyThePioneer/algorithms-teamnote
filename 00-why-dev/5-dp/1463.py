#1463 1로 만들기

import sys

# 정수 N 입력받기
n = int(sys.stdin.readline())

# dp table 초기화
dp = [0] * (n + 1)

# dp 진행
for i in range(2, n + 1):

    # 먼저 1을 빼는 연산
    dp[i] = dp[i - 1] + 1

    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# 최소 연산 횟수 출력
print(dp[n])