#1012 유기농 배추

import sys
sys.setrecursionlimit(10000) # 재귀

# dfs 함수
def dfs(x, y):
    # 상하좌우 방향
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        # 현재 배추의 상하좌우로 이동해서
        nx = x + dx[i]
        ny = y + dy[i]

        # 배추인 경우 DFS 실행
        if (0 <= nx < M) and (0 <= ny < N):
            if field[ny][nx] == 1:
                field[ny][nx] = 0 # 1을 0으로 바꾼다
                dfs(nx, ny)

# 테스트 케이스의 수 T 입력받기
T = int(sys.stdin.readline())

# 각 테스트 케이스의 배추밭의 가로 길이 M, 세로 길이 N, 배추 개수 K 입력받기
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    # 배추밭 이중 리스트 선언 후 0으로 초기화하기
    field = [[0 for _ in range(M)] for _ in range(N)]
    worm = 0

    # K개의 배추 위치 정보 입력받아서 1로 표시하기
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        field[Y][X] = 1

    # 배추밭[0][0]부터 배추밭[M-1][N-1]까지 돌면서
    for x in range(M):
        for y in range(N):
            # 배추인 경우 지렁이를 한 마리 추가하고 DFS 실행
            if field[y][x] == 1:
                worm += 1
                dfs(x, y)

    # 총 지렁이의 수 출력
    print(worm)