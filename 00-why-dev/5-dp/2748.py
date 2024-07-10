#2748 피보나치 수 2

import sys

# 자연수 n 입력받기
n = int(sys.stdin.readline())

# dp table을 만들고, dp[0] = 0, dp[1] = 1, dp[2] = 1 넣기
dp = [0, 1, 1]

# for문을 돌며 dp[3]부터 dp[n]까지 계산하기
for i in range(3, n + 1):
    dp.append(dp[i - 2] + dp[i - 1])

# dp[n] 출력하기
print(dp[n])