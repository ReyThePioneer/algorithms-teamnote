#1388 바닥 장식

import sys

# 방바닥 세로 크기 N, 가로 크기 M 입력받기
n, m = map(int, sys.stdin.readline().split())

# 바닥 장식 모양 입력받기
floor = []
for _ in range(n):
    floor.append(list(sys.stdin.readline()))

# 나무 판자 개수
cnt = 0

# 바닥 장식 모양이 -일 때 오른쪽으로 탐색
for i in range(n):
    a = ""
    for j in range(m):
        if floor[i][j] == "-" and floor[i][j] != a:
            cnt += 1
        a = floor[i][j]
                                        
# 바닥 장식 모양이ㅣ일 때 아래쪽으로 탐색
for j in range(m):
    a = ""
    for i in range(n):
        if floor[i][j] == '|' and floor[i][j] != a:
            cnt += 1
        a = floor[i][j]

# 총 나무 판자 개수 출력
print(cnt)