#2606 바이러스

import sys

# 컴퓨터의 수 입력받기 (1 ≤ n ≤ 100)
n = int(sys.stdin.readline())

# 네트워크 상 직접 연결되어 있는 컴퓨터 쌍의 수 입력받기
v = int(sys.stdin.readline())

# 네트워크 상 직접 연결되어 있는 컴퓨터의 번호 쌍들 입력받기
graph = [[] for _ in range(n + 1)] # 1번 컴퓨터가 1번 인덱스
visited = [0] * (n + 1) # 방문 1, 미방문 0
for _ in range(v):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결(양방향)

# DFS
def dfs(v): # 방문할 컴퓨터 번호 v 입력받기
    visited[v] = 1 # 방문 처리
    for nx in graph[v]: # v번 컴퓨터에 연결된 컴퓨터들
        if visited[nx] == 0: # 방문 여부 검사
            dfs(nx) # 방문 안 했을 시 재귀
dfs(1) # 1번 컴퓨터부터 방문
print(sum(visited) - 1) # 1번 컴퓨터를 제외한 컴퓨터 개수 출력