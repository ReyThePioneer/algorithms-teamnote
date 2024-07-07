#10816 숫자 카드 2

import sys
from bisect import bisect_left, bisect_right

# 상근이가 가지고 있는 카드의 수 N 입력받기
n = int(sys.stdin.readline())
# N개의 카드 숫자들 입력받기
cards = list(map(int, sys.stdin.readline().split()))
# 상근이가 가지고 있는 카드 오름차순 정렬하기
cards.sort()

# 비교할 숫자의 개수 M과, M개의 정수들 입력받기
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

# 비교할 각 숫자들에 대해 이분탐색으로 개수 세기
result = []
for target in targets:
    # target보다 크거나 같은 첫 번째 위치
    left_index = bisect_left(cards, target)
    # target보다 큰 첫 번째 위치
    right_index = bisect_right(cards, target)
    # target의 개수
    result.append(right_index - left_index)

# targets의 각 숫자가 cards에 몇 개씩 있는지 결과 출력
print(' '.join(map(str, result)))