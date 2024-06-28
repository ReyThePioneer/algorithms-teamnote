#25305 커트라인

import sys

# 응시자의 수 N, 상을 받는 사람의 수 k 입력받기
n, k = map(int, sys.stdin.readline().split())

# 각 학생의 점수 x 입력받기
x = list(map(int, sys.stdin.readline().split()))

# 각 학생의 점수를 내림차순 정렬하기
x.sort(reverse=True)

# (k - 1)번째 점수 출력하기
print(x[k - 1])