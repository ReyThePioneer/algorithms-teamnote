#1931 회의실 배정

import sys

# 회의의 수
n = int(sys.stdin.readline())

# 각 회의의 정보
info = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    info.append([start, end])

# 회의가 끝나는 시간으로 정렬
info.sort(key=lambda x: (x[1], x[0]))

# 첫 번째 회의는 선택하고 시작
cnt = 1
# 첫 번째 회의의 끝나는 시간
end = info[0][1]

# 두 번째 회의부터
for i in range(1, n):
    # 이전 회의 끝나는 시간 <= 시작 시간
    if end <= info[i][0]:
        end = info[i][1]
        cnt += 1

# 선택한 회의 개수의 합
print(cnt)