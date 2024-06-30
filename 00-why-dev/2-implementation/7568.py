#7568 덩치

import sys

# 전체 사람의 수(N) 입력받기
n = int(sys.stdin.readline())

# 각 사람의 덩치 정보, 등수 정보를 저장할 배열
builds = []
ranks = [0] * n

# 각 사람의 몸무게와 키(x y) 2차원 배열에 입력받기
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    builds.append([x, y])

# 각 사람보다 덩치가 큰 사람의 수 계산
for i in range(n):
    cnt = 0
    for j in range(n):
        if builds[i][0] < builds[j][0] and builds[i][1] < builds[j][1]:
            cnt += 1
        ranks[i] = cnt + 1

# 각 사람의 덩치 등수 출력
print(" ".join(map(str, ranks)))