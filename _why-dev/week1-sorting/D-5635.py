#5635 생일

import sys

# 학생 수 n 입력받기
n = int(sys.stdin.readline())

# 각 학생의 이름과 생년월일 입력받기
births = []
for _ in range(n):
    name, d, m, y = sys.stdin.readline().split()
    births.append([int(y), int(m), int(d), name])

# 년, 월, 일 순으로 정렬하기 (나이가 많은 순)
births.sort()

# 마지막번째 학생의 이름 출력하기
print(births[n - 1][3])

# 첫 번째 학생의 이름 출력하기
print(births[0][3])