# 자원 캐기

n, m = map(int, input().split())

mine = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + mine[i-1][j-1]

print(dp[n][m])