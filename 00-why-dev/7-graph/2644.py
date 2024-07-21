#2644 촌수계산

import sys

# 전체 사람의 수 n, 촌수 계산할 두 사람의 번호 a,b, 부모 자식 간 관계 개수 m 입력받기
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

# 부모 자식 간 관계 x,y 입력받기
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
kin = []

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS 정의 : 촌수 = a부터 b까지의 거리
def dfs(v, cnt):
    cnt += 1
    visited[v] = 1

    if v == b:
        kin.append(cnt)
    
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i, cnt)

# DFS 실행
dfs(a, 0)

# 결과 출력
if len(kin) == 0:
    print(-1)
else:
    print(kin[0] - 1)