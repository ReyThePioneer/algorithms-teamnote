#1260 DFS와 BFS

import sys

# 정점의 개수 N, 간선의 개수 M, 시작 정점 번호 V 입력받기
N, M, V = map(int, sys.stdin.readline().split())

# M개의 줄에 간선이 연결하는 두 정점의 번호 입력받기
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 (노드가 스택에 들어간 적 있는지)
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

# DFS 함수
def dfs(V):
    visited_dfs[V] = 1 # 방문 처리
    print(V, end=' ') # 방문 노드 출력
    for i in range(1, N + 1): # 연결된 노드 탐색
        if graph[V][i] == 1 and visited_dfs[i] == 0:
            dfs(i)

# BFS 함수
def bfs(V):
    queue = [V] # 큐 이용
    visited_bfs[V] = 1 # 방문 처리
    while queue: # 큐에 값이 없을 때까지
        V = queue.pop(0) # 큐에서 방문 노드 삭제
        print(V, end=' ') # 방문 노드 출력
        for i in range(1, N + 1): # 연결된 노드 탐색
            if graph[V][i] == 1 and visited_bfs[i] == 0:
                queue.append(i) # 큐에 넣기
                visited_bfs[i] = 1 # 방문 처리

# DFS, BFS 실행
dfs(V)
print()
bfs(V)
