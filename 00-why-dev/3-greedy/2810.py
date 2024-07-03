#2810 컵홀더

import sys

# 좌석의 수 N 입력받기
n = int(sys.stdin.readline())

# 좌석 정보 입력받기
seats = sys.stdin.readline()

# 커플석 세기
num_couple_seat = seats.count("LL")

# 커플석 LL이 1개일 때는 모든 사람이 컵을 놓을 수 있음
if num_couple_seat <= 1:
    print(n)
# 커플석이 2개 이상인 경우, LL이 1개 늘어날 때마다 1명이 컵을 못 놓게 됨
else:
    print(n - num_couple_seat + 1)