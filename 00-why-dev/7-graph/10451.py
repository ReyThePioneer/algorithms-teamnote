#10451 순열 사이클

import sys

# dfs 함수 정의
def dfs(v):
    visited[v] = 1 # v 노드 방문 처리
    next = permu[v] # 다음 노드 정보 가져오기
    if visited[next] == 0: # 다음 노드가 있다면 재귀로 이동
        dfs(next)
    return

# 테스트 케이스의 개수 T 입력받기
t = int(sys.stdin.readline())

# 각 테스트 케이스마다 순열의 크기 N, permu 리스트에 순열 입력받기
for _ in range(t):
    n = int(sys.stdin.readline())
    permu = [0] + list(map(int, sys.stdin.readline().split()))

    # visited와 cycle_cnt 초기화
    visited = [0] * (n + 1)
    cycle_cnt = 0

    # 1부터 N까지 미방문 노드이면 dfs 실행 후 사이클 개수 추가
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i) # dfs 실행
            cycle_cnt += 1
    print(cycle_cnt)