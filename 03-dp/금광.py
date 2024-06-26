# <문제> 금광

# test case의 수 입력받기
T = int(input())

# 금광 정보 입력받기
for _ in range(T):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # dp를 위한 2차원 dp table 초기화
    dp = []
    index = 0

    # 금광정보 m개씩 슬라이싱 해서 dp table에 담기
    for _ in range(n):
        dp.append(array[index:index + m])
        index += m
    
    # dp 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n: left_down = 0
            else: left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)