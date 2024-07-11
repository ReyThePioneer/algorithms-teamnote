#2775 부녀회장이 될테야

import sys

# 테스트 케이스의 수 T 입력받기
T = int(sys.stdin.readline())

# 각 테스트케이스마다 층/호수 정보 입력받기
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    # 0층 리스트 만들기 (1호 ~ n호)
    apart = [x for x in range(1, n + 1)]

    # k층 리스트 만들기 (1호 ~ n호)
    for _ in range(k):
        for j in range(1, n):
            apart[j] += apart[j - 1] # 여기가 핵심!

    # k층 n호 사람 수 출력 (리스트에서 가장 마지막 원소)
    print(apart[-1])