#2828 사과 담기 게임

import sys

# 스크린의 칸 개수 N, 바구니의 칸 개수 M 입력받기
n, m = map(int, sys.stdin.readline().split())

# 떨어지는 사과의 개수 J 입력받기
j = int(sys.stdin.readline())

# J개의 사과가 떨어지는 위치 입력받기
apples = []
for _ in range(j):
    apples.append(int(sys.stdin.readline()))

dis = 0 # 바구니가 움직인 거리
now = 1 # 현 위치

for apple in apples:
    # 현 위치에 가만히 있어도 사과를 받을 수 있는 경우
    if (now <= apple) and (now + (m-1) >= apple):
        pass
    # 왼쪽으로 이동해야 사과를 받을 수 있는 경우
    elif now > apple:
        dis += abs(now - apple)
        now = apple
    # 오른쪽으로 이동해야 사과를 받을 수 있는 경우
    else:
        dis += apple - (m-1) - now
        now = apple - (m-1)

# 총 이동 거리 출력
print(dis)