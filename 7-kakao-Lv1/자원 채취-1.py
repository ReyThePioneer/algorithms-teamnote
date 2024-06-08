# 지도의 크기 n x m 입력받기
n, m = map(int, input().split())

# 지도에 존재하는 자원 정보 입력 받기
map = [list(map(int, input().split())) for _ in range(n)]

# DP table
dp = [[0] * (m + 1) for _ in range(n + 1)]

# DP table 채우기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + map[i-1][j-1]

# 가장 마지막 칸이 답
print(dp[n][m])