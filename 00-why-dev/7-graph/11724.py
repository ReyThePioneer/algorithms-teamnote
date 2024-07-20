#11724 연결 요소의 개수

import sys
sys.setrecursionlimit(10**6)

# 정점의 개수 N, 간선의 개수 M 입력받기
N, M = map(int, sys.stdin.readline().split())

# M개의 (u, v) 입력받기
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs 함수 정의
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

# 연결 요소의 개수 출력하기
visited = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)
print(cnt)