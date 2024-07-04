#14916 거스름돈

import sys

# 거스름돈 액수 n 입력받기
n = int(sys.stdin.readline())

# 거스름돈 동전 개수
cnt = 0

while True:
    # 거슬러줄 수 없는 경우
    if n < 0:
        cnt = -1
        break

    # 일단 5원으로 거슬러주기
    if n % 5 == 0:
        cnt += n // 5
        break
    # 나머지는 2원으로 거슬러주기
    else:
        n -= 2
        cnt += 1

# 거슬러줄 수 있는 경우 최소 동전의 개수 출력
# 거슬러줄 수 없는 경우 -1 출력
print(cnt)