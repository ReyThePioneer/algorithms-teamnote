#10814 나이순 정렬

import sys

# 회원 수 N 입력받기
n = int(sys.stdin.readline())

# N명의 회원 정보(나이, 이름) 입력받기
info = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    # 나이의 자료형은 int로
    info.append([int(age), name])

# 나이를 기준으로 오름차순 정렬하기
info.sort(key=lambda x:x[0])

# [나이 이름] 출력하기
for i in info:
    print(i[0], i[1])