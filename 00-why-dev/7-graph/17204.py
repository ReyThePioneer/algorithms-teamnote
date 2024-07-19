#17204 죽음의 게임

import sys

# 참석자 수 N, 보성이의 번호 K 입력받기
N, K = map(int, sys.stdin.readline().split())

# N개의 지목 번호 입력받기
numlist = [int(sys.stdin.readline()) for _ in range(N)]

point = 0 # 지목하는 사람 : 0부터
M = 0 # 지목 횟수 : 0부터 M까지

for i in range(N):
    target = numlist[point] # 지목당한 사람
    M += 1 # 지목 횟수 증가
    if target == K: # 보성이 걸리면
        print(M)
        break
    point = target # 이제 지목당한 사람이 지목하는 사람 됨
else: # 보성이가 안 걸리면
    print(-1)